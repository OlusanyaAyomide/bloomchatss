from nturl2path import url2pathname
from django.urls import path
from . import views

# urlpatterns=[
#     path("",views.home,name="home"),
#     path("login",views.loginpage,name="login"),
#     path("logout",views.logoutpage,name="logout"),
#     path("create",views.create_room,name="create-room"),
#     path("chatroom/<str:id>",views.room_view,name="room-view"),
#     path("edit-room/<str:id>",views.edit_room,name="edit"),
#     path("delete-room/<str:id>",views.delete_room,name="delete-room"),
#     path("join-room/<str:id>",views.join_room,name="join"),
#     path("exit-room/<str:id>",views.leave_room,name="leave"),
#     path("create-message/<str:id>",views.create_message,name="create-message"),
#     path("edit-room/<str:m_id>/<str:room_id>",views.edit_message,name="edit-room"),
#     path("delete-message/<str:id>",views.delete_message,name="delete-message"),
#     path("profile",views.profilelogin,name="profilelogin"),
#     path("profile-view/<int:id>",views.room_redirect,name="room_redirect"),
#     path("profile-view/<str:slug>",views.profile_view,name="profile"),
#     path("follow/<str:slug>",views.follow,name="follow"),
#     path("unfollow/<str:slug>",views.unfollow,name="unfollow"),
#     path("signup",views.user_creation,name="user_creation"),
#     path("edit-profile/<str:slug>",views.edit_profile,name="edit_profile"),
#     path("replies/<str:id>",views.reply_message,name="reply"),
#     path("create-reply/<str:id>",views.create_reply,name="create-reply"),
#     path("edit-reply/<str:slug>/<str:re_slug>",views.edit_reply,name="edit-reply"),
#     path("delete-reply/<str:slug>/<str:re_slug>",views.delete_reply,name="delete-reply"),
#     path("profile-search/<str:slug>",views.profile_search,name="profile_search"),
#     path("private-mesage/<str:slug>",views.private_message,name="private_message"),
#     path("create-topic",views.create_topic,name="new_topic"),
#     path('superuser0372',views.superuser,name='superuser'),
#     path('jumper0372',views.superb),
#     path('notification/<str:view>/<str:path>',views.notify,name='notify'),
#     path('like/<str:id>',views.like_message,name='like'),
#     path('unlike/<str:id>',views.unlike_message,name='unlike'),
#     path('private/<str:slug>',views.private_view,name='private'),
#     path('private_message/<str:slug>',views.private_message,name='message'),
#     path('chat/<str:slug>',views.chat_count,name='chat'),
#     path('room-search',views.room_search,name='room_search'),
 
# ]
urlpatterns = [
    path('',views.demo)
]
