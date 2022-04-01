
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('post/<str:pk>/',views.post,name="post"),
    path('posts/',views.posts,name="posts"),
    path('sendEmail/',views.sendEmail,name="sendEmail"),


    path('createpost/',views.createpost,name="createpost"),
    path('post/<str:pk>/comment',views.comment,name="comment"),


    path('createuser/',views.createuser,name="createuser"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
]