
from tempfile import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="home"),
    path('post/<str:pk>/',views.post,name="post"),
    path('posts/',views.posts,name="posts"),
        path('changepassword/',views.changepassword,name="changepassword"),

    path('createpost/',views.createpost,name="createpost"),
    path('updatePost/<str:pk>/',views.updatePost,name="updatePost"),
    path('deletePost/<str:pk>/',views.deletePost,name="deletePost"),
    
    
    path('sendEmail/',views.sendEmail,name="sendEmail"),


    path('createuser/',views.createuser,name="createuser"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    
    
    
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="OurProfile/password_reset.html"), name="password_reset"),
    path(
        "password-reset-done",
        auth_views.PasswordResetDoneView.as_view(template_name="OurProfile/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="OurProfile/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="OurProfile/password_reset_complete.html"),
        name="password_reset_complete",
    ),
]