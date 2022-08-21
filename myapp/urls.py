from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),]
#     path("login",views.loginpage,name="login"),
#     path("logout",views.logoutpage,name="logout"),
#     path("create",views.create_room,name="create-room"),
#     path("chatroom/<str:slug>",views.room_view,name="room-view"),
#     path("edit-room/<str:slug>",views.edit_room,name="edit"),
#     path("delete-room/<str:slug>",views.delete_room,name="delete-room"),
#     path("join-room/<str:slug>",views.join_room,name="join"),
#     path("exit-room/<str:slug>",views.leave_room,name="leave"),
#     path("create-message/<str:slug>",views.create_message,name="create-message"),
#     path("edit-room/<str:slug>/<str:room_slug>",views.edit_message,name="edit-room"),
#     path("delete-message/<str:slug>",views.delete_message,name="delete-message"),
#     path("profile",views.profilelogin,name="profilelogin"),
#     path("profile-view/<int:id>",views.room_redirect,name="room_redirect"),
#     path("profile-view/<str:slug>",views.profile_view,name="profile"),
#     path("follow/<str:slug>",views.follow,name="follow"),
#     path("unfollow/<str:slug>",views.unfollow,name="unfollow"),
#     path("signup",views.user_creation,name="user_creation"),
#     path("edit-profile/<str:slug>",views.edit_profile,name="edit_profile"),
#     path("replies/<str:slug>",views.reply_message,name="reply"),
#     path("create-reply/<str:slug>",views.create_reply,name="create-reply"),
#     path("edit-reply/<str:slug>/<str:re_slug>",views.edit_reply,name="edit-reply"),
#     path("delete-reply/<str:slug>/<str:re_slug>",views.delete_reply,name="delete-reply"),
#     path("profile-search/<str:slug>",views.profile_search,name="profile_search"),
#     path("latest/<int:id>",views.recent_room,name="most_recent"),
#     path("private-mesage/<str:slug>",views.private_message,name="private_message"),
#     path("create-topic",views.create_topic,name="new_topic"),
# ]