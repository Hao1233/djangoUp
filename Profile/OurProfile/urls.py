
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('post/<slug:slug>/',views.post,name="post"),
    path('posts/',views.posts,name="posts"),

    path('createpost/',views.createpost,name="createpost"),
    path('updatePost/<slug:slug>/',views.updatePost,name="updatePost"),
    #path('deletePost/',views.deletePost,name="deletePost"),
    
    
    path('sendEmail/',views.sendEmail,name="sendEmail"),
    path('post/<slug:slug>/comment',views.comment,name="comment"),


    path('createuser/',views.createuser,name="createuser"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
]