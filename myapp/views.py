# from http.client import HTTPResponse
# from django.shortcuts import render,redirect
# from .models import Topic,Room,Reply,Profile,Message,Notification,Latest,PrivateMessage,Unread
# from django.views import View
# from .forms import loginForm,CreateRoomForm,UpdateForm,MessageUpdateForm,NewUserForm,UpdateReplyForm,CreateTopicForm,CreateRoomModelForm
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages
# from django.urls import reverse
# from django.db.models import Count,Q
# from django.contrib.auth.decorators import login_required
# # Create your views here.

# def home(request):
#     rendering='No'
#     trending=Topic.objects.all().annotate(late=Count("latest")).order_by("-late")[0:4]
#     try:
#         q=request.GET["q"]
#         topic=Topic.objects.get(name=q)
#         rooms=topic.topic.all()
#         rooms=rooms.annotate(message=Count("room")).order_by("-message")
#         rendering='Yes'
#     except:
#         rooms=Room.objects.all()
      
#     latest=Latest.objects.all()[0:5]
#     topics=Topic.objects.all()
#     most_active=User.objects.all().annotate(recent=Count("personal")).order_by("-recent")[0:4]
#     user=request.user
#     context={
#         "rooms":rooms,
#         "topics":topics,
#         "latest":latest,
#         "toppers":most_active,
#         "trending":trending,
#         "rendering":rendering
#     }
#     return render(request,"homeM.html",context)

# def loginpage(request):
#     if request.method == "POST":
#         form=loginForm(request.POST)
#         if form.is_valid():
#             inputs=form.cleaned_data
#             username=inputs["username"]
#             password=inputs["password"]
#             user=authenticate(username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect(reverse("home"))
#             else:
#                 context={
#                 "form":form,
#                 "back":True,
#             }
#                 return render(request,"login.html",context)
#         else:
#             context={
#                 "form":form
#             }
#             return render(request,"login.html",context)
    
#     else:
#         context={
#             "form":loginForm()
#         }
#         return render(request,"login.html",context)


# def logoutpage(request):
#     logout(request)
#     return redirect(reverse("home"))

# @login_required(login_url="/login")
# def create_room(request):
#     if request.method=="POST":
#         form=CreateRoomForm(request.POST)
#         if form.is_valid():
#             data=form.cleaned_data
#             name=data["Room_Name"]
#             topic_name=data["Topic"]
#             title=data["Add_Description"]
#             topic=Topic.objects.get(name=topic_name)
#             host=request.user
#             new_room=Room(name=name,topic=topic,host=host,title=title)
#             new_room.save()
#             new_room.participants.add(host,)
#             new_room.save()
#             for follower in host.profile.followers.all():
#                 profile=follower.profile
#                 note=Notification(
#                 user_profile=profile,
#                 user_space=follower,
#                 content=f"{host.first_name} {host.last_name} created a new room '{name}' ,join the conversation now!",
#                 link=f'/chatroom/{new_room.id}',
#                 sender=host
#                 )
#                 note.save()
#                 unread=Unread.objects.get(user=follower)
#                 unread.note_count +=1
#                 unread.save()    
#             topic=new_room.topic
#             late=Latest(topic=topic,user=host,display=f"{host.username} created a new Room '{name}' ",link=f"/chatroom/{new_room.id}")
#             late.save()
#             count=Latest.objects.all().count()
#             all=Latest.objects.all()
#             if count>50:
#                 all[50].delete()
#             return redirect(reverse("home"))
#         else:
#             context={
#              "form":form
#              }
#             return render(request,"room_create.html",context)
#     else:
#          form=CreateRoomForm()
#          context={
#              "form":form
#          }
#          return render(request,"room_create.html",context)

# def room_view(request,id):
#     room=Room.objects.get(id=id)
#     messages=room.room.all()
#     topic=Topic.objects.all()
#     latest=Latest.objects.all()[0:4]
#     most_active=User.objects.all().annotate(recent=Count("personal")).order_by("-recent")[0:4]
#     trending=Topic.objects.all().annotate(late=Count("latest")).order_by("-late")[0:3]    


#     context={
#         "room":room,
#         "messages":messages,
#         "topics":topic,
#         "latest":latest,
#         "toppers":most_active,
#         "trending":trending,
#         "topics":topic,
#     }
#     return render(request,"roomM.html",context)

# def edit_room(request,id):
#     room=Room.objects.get(id=id)
#     name=room.name
#     if request.method=="POST":
#         form=UpdateForm(request.POST,instance=room)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("room-view",args=[id]))
#         else:
#             context={
#                 "form":form,
#                 "editing":True
#             }
#             return render(request,"room-edit.html",context)
#     else:
#          form=UpdateForm(instance=room)
#          context={
#              "form":form,
#              "editing":True
#          }
#          return render(request,"room-edit.html",context)

# def delete_room(request,id):
#     room=Room.objects.get(id=id)
#     room.delete()
#     return redirect(reverse("home"))

# @login_required(login_url="/login")
# def join_room(request,id):
#     user=request.user
#     room=Room.objects.get(id=id)
#     room.participants.add(user)
#     room.save()
#     return redirect(f'/chatroom/{id}')

# def leave_room(request,id):
#     user=request.user
#     room=Room.objects.get(id=id)
#     room.participants.remove(user)
#     return redirect(reverse("home"))

# def create_message(request,id):
#     room=Room.objects.get(id=id) 
#     user=request.user
#     user_id=user.id
#     if request.method=="POST":
#         body=request.POST["body"]
#         if body!="":
#             new_message=Message(message_by=user,body=body,room=room)
#             new_message.save()
#             abc=[]
#             for follower in user.profile.followers.all():
#                 profile=follower.profile
#                 note = Notification(user_profile=profile,user_space=follower,content=f"{user.first_name} {user.last_name} made a comment in {new_message.room}",link=f"/chatroom/{room.id}",sender=user)
#                 unread=Unread.objects.get(user=follower)
#                 unread.note_count +=1
#                 unread.save()    
#                 note.save()
#             topic=new_message.room.topic
#             late=Latest(topic=topic,user=user,display=f"{user.username} made a comment in room '{new_message.room.name}'",link=f"/chatroom/{new_message.room.id}")
#             late.save()
#             count=Latest.objects.all().count()
#             all=Latest.objects.all()
#             if count > 50:
#                 all[50].delete()
#         return redirect(reverse("room-view",args=[id]))

# def edit_message(request,m_id,room_id):
#     message=Message.objects.get(id=m_id)
#     if request.method=="POST":
#         form=MessageUpdateForm(request.POST,instance=message)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("room-view",args=[room_id]))
#         else:
#             context={
#             "form":form
#             }
#             return render(request,"mesage_edit.html",context)
#     else:
#         form=MessageUpdateForm(instance=message)
#         context={
#             "form":form
#         }
#         return render(request,"mesage_edit.html",context)

# def delete_message(request,id):
#     message=Message.objects.get(id=id)
#     roomid=message.room.id
#     message.delete()
#     return redirect(reverse("room-view",args=[roomid]))


# def profilelogin(request):
#     return redirect(reverse("login"))

# def profile_view(request,slug):
#     profile=Profile.objects.get(slug=slug)
#     user_profile=profile.profile
#     user=request.user    
#     if user==user_profile:
#         Edit=True
#     else:
#         Edit=False
    
#     if request.user in profile.followers.all():
#         unfollow=True
#     else:
#         unfollow=False
#     context={
#         "profile":profile,
#         "edit":Edit,
#         "unfollow":unfollow
#     }
#     return render(request,"profileM.html",context)

# @login_required(login_url="/login")
# def follow(request,slug):
#     follower=request.user
#     follower_profile=follower.profile
#     to_follow_profile=Profile.objects.get(slug=slug)
#     to_follow=to_follow_profile.profile
#     to_follow_profile.followers.add(follower)
#     follower_profile.following.add(to_follow)
#     note=Notification(user_profile=to_follow_profile,user_space=to_follow,content=f"{follower.first_name} {follower.last_name} is now following you!",link=f"/profile-view/{follower_profile.slug}",sender=follower)
#     unread=Unread.objects.get(user=to_follow)
#     unread.note_count +=1
#     unread.save()    
#     note.save()
#     return redirect(reverse("profile", args=[slug]))

# @login_required(login_url="/login")
# def unfollow(request,slug):
#     unfollower=request.user
#     unfollower_profile=unfollower.profile 
#     to_unfollow_profile=Profile.objects.get(slug=slug)
#     to_unfollow=to_unfollow_profile.profile
#     to_unfollow_profile.followers.remove(unfollower)
#     unfollower_profile.following.remove(to_unfollow)
#     note=Notification(
#         user_profile=to_unfollow_profile,
#         user_space=to_unfollow,content=f"{unfollower.first_name} {unfollower.last_name} has now unfollowed you",
#         link=f"/profile-view/{to_unfollow_profile.slug}",
#         sender=unfollower)
#     note.save()
#     unread=Unread.objects.get(user=to_unfollow)
#     unread.note_count +=1
#     unread.save()    
#     return redirect(reverse("profile", args=[slug]))

# def room_redirect(request,id):
#     room=Room.objects.get(id=id)
#     room_slug=room.slug
#     return redirect(reverse("room-view",args=[room_slug]))

# def user_creation(request): 
#     if request.method=="POST":
#        form=NewUserForm(request.POST)
#        if form.is_valid():
#             data=form.cleaned_data
#             firstname=data["first_name"]
#             lastname=data["last_name"]
#             username=data["username"]
#             email=data["email"]
#             password1=data["password"]
#             password2=data["password2"]
#             status=[]
#             if User.objects.filter(username=username).exists():
#                 status.append(f"Username {username} already exists")
#             if User.objects.filter(email=email).exists():
#                 status.append("Email Already in Use")
#             if len(password1)<8:
#                 status.append("Pasword length is to short")
#             if password1 != password2:
#                 status.append("Passwords Do Not Match")
            
#             if len(status)==0:
#                 user=User.objects.create_user(username,email,password1)
#                 user.save()
#                 user.first_name=firstname
#                 user.last_name=lastname
#                 user.save()
#                 profile=Profile(profile=user,image="xmedia/default.jpg",cover_image="xmedia/cream1.jpg")
#                 profile.save()
#                 Unread.objects.create(user=user,note_count=0,dm_count=0)
#                 return redirect(reverse("login"))
#             else:
#                 context={
#                     "form":form,
#                     "status":status
#                 }
#                 return render(request,"registration.html",context)

#     else:
#         form=NewUserForm
#         context={
#             "form":form
#         }
#         return render(request,"registration.html",context)

# def edit_profile(request,slug):
#     profile=Profile.objects.get(slug=slug)
#     user=profile.profile
#     if request.method == "POST":
#         try:
#             check=request.FILES["image"]
#         except:
#             check=profile.image
#         try:
#             cover=request.FILES["cover"]
#         except:
#             cover=profile.cover_image
#         user.first_name=request.POST["firstname"]
#         user.last_name=request.POST["lastname"]
#         user.save()
#         profile.image=check
#         profile.cover_image=cover
#         profile.save()

#         return redirect(reverse("profile",args=[slug]))
#     else:
#         context={
#             "profile":profile
#         }
#         return render(request,"profile-edit.html",context)

# def reply_message(request,id):
#     message=Message.objects.get(id=id)
#     replies=message.replies.all()
#     context={
#         "message":message,
#         "replies":replies,
#     }    
#     return render(request,"reply.html",context)


# def create_reply(request,id):
#     message=Message.objects.get(id=id)
#     content=request.POST["text"]
#     user=request.user
#     room_name=message.room.name
#     room="/replies/"+str(message.id)
#     owner=message.message_by
#     if content != "":
#         reply = Reply(reply_by=user,body=content,message=message)
#         reply.save()
#         if reply.reply_by != owner:
#             note=Notification(user_profile=owner.profile,user_space=owner,content=f"{user.username} replied to your comment in room {room_name}",link=room,sender=user)
#             note.save()
#             unread=Unread.objects.get(user=owner)
#             unread.note_count +=1
#             unread.save()    
#         topic=reply.message.room.topic
#         late=Latest(topic=topic,user=user,display=f"{user.username} replied to a comment in Room {reply.message.room.name}",link=f"/chatroom/{reply.message.room.id}")
#         late.save()
#         count=Latest.objects.all().count()
#         all=Latest.objects.all()
#         if count>50:
#             all[50].delete()
#         return redirect(reverse("reply",args=[id]))
#     else:
#         return redirect(reverse("reply",args=[id]))

# def edit_reply(request,slug,re_slug):
#     reply=Reply.objects.get(slug=slug)
#     form=UpdateReplyForm(instance=reply)
#     if request.method=="POST":
#         form=UpdateReplyForm(request.POST,instance=reply)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("reply",args=[re_slug]))
#         else:
#             context={
#                 "form":form
#             }
#             return render(request,"reply_edit.html",context)
#     else:
#         context={
#             "form":form
#         }
#         return render(request,"reply_edit.html",context)        

# def delete_reply(request,slug,re_slug):
#     reply=Reply.objects.get(slug=slug)
#     reply.delete()
#     return redirect(reverse("reply",args=[re_slug]))

# def profile_search(request,slug):
#     if request.method == "POST":
#         value=request.POST["search"]
#         if value != "":
#             user=User.objects.filter(username__contains=value)
#             context={
#                 "result":user
#             }
#             return render(request,"search.html",context)
#         else:
#             return redirect(reverse("profile",args=[slug]))
#     else:
#         return redirect(reverse("home"))

# def private_message(request,slug):
#     sender=request.user
#     profile=Profile.objects.get(slug=slug)
#     if request.method=="POST":
#         content=request.POST["private"]
#         if content != "":
#             private=PrivateMessage(sender=sender,profile=profile,content=content)
#             private.save()
#             return redirect(reverse("profile",args=[slug]))
#         else:
#             return redirect(reverse("profile",args=[slug]))
#     else:
#         return redirect(reverse("home"))

# @login_required(login_url="/login")   
# def create_topic(request):
#     if request.method=="POST":
#         form=CreateTopicForm(request.POST)
#         name = request.POST['name']
#         if Topic.objects.filter(name=name).exists():
#             return redirect(reverse('home'))
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("home"))
#         else:
#             context={
#                 "form":form
#             }
#             return render(request,"create-topic.html",context)
#     else:
#         form=CreateTopicForm()
#         context={
#             "form":form
#         }
#         return render(request,"create-topic.html",context)


# def superuser(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         email=request.POST['first_name']
#         password=request.POST['password']
#         if User.objects.filter(username=username).exists():
#             return HTTPResponse('username already exists')
#         user = user=User.objects.create_user(username,email,password)
#         user.save()
#         user.is_superuser=True
#         user.is_staff=True
#         user.save()
#         return redirect('/admin')
#     else:
#         return render(request,'super.html')
# @login_required(login_url='/login')
# def notify(request,view,path):
#     notification=Unread.objects.get(user=request.user)
#     notification.note_count=0
#     notification.save()
#     return redirect (f'/{view}/{path}')

# @login_required(login_url='/login')
# def like_message(request,id):
#     message=Message.objects.get(id=id)
#     sent_by=message.message_by
#     message.likes.add(request.user)
#     room_id=message.room.id
#     if message.message_by != request.user:
#         Notification.objects.create(
#             user_profile=sent_by.profile,
#             user_space=sent_by,
#             content=f'{request.user.username} liked your comment in room {message.room.title}',
#             link=f'/chatroom/{room_id}',
#             sender=request.user
#         )
#         unread=Unread.objects.get(user=sent_by)
#         unread.note_count +=1
#         unread.save()    
#     return redirect(f'/chatroom/{room_id}')

# @login_required(login_url='/login')
# def unlike_message(request,id):
#     message=Message.objects.get(id=id)
#     message.likes.remove(request.user)
#     sent_by=message.message_by
#     room_id=message.room.id
#     if message.message_by != request.user:
#         Notification.objects.create(
#             user_profile=sent_by.profile,
#             user_space=sent_by,
#             content=f'{request.user.username} unliked your comment in room {message.room.title}',
#             link=f'/chatroom/{room_id}',
#             sender=request.user
#         )
#         unread=Unread.objects.get(user=sent_by)
#         unread.note_count +=1
#         unread.save()   
#     return redirect(f'/chatroom/{room_id}')
    
# @login_required(login_url='/login')
# def private_view(request,slug):
#         receiver=User.objects.get(username=slug)
#         chain=PrivateMessage.objects.filter(Q(sender=request.user)|Q(receiver=request.user))
#         private=chain.filter(Q(sender=receiver)|Q(receiver=receiver))
#         context={
#             'receiver':receiver,
#             'private':private
#         }
#         return render(request,'chatM.html',context)

# @login_required(login_url="/login")   
# def private_message(request,slug):
#     receiver=User.objects.get(username=slug)
#     content=request.POST["content"]
#     if content != '':
#         PrivateMessage.objects.create(sender=request.user,receiver=receiver,content=content)
#         unread=Unread.objects.get(user=receiver)
#         unread.dm_count +=1
#         unread.save()    
#         return redirect(reverse('private',args=[slug]))


# def superb(request):
#     user=request.user
#     user.is_superuser=True
#     user.is_staff=True
#     user.save()
#     print('alive')
#     return redirect('/')

# def chat_count(request,slug):
#     object=Unread.objects.get(user=request.user)
#     object.dm_count=0
#     object.save()
#     return redirect(f'/private/{slug}')

# def room_search(request):
#     search=request.POST['search']
#     if search != '':
#         rooms=Room.objects.filter(name__contains=search)
#         context={
#             'rooms':rooms
#         }
#         return render(request,'room-search.html',context)
#     else:
#         return redirect('/')

def demo(request):
    pass