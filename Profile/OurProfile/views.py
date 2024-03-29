
from turtle import pos
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .models import *
from .forms import CreatePostForm,CreateUserForm, CreateCommentForm, ChangePassword
from .filters import FiltersForms
from .decoratores import unauthenticated_user
def home(request):
    posts = Post.objects.all()[0:3]
    context = {'posts':posts}
    return render(request,"OurProfile/home.html",context)
def posts(request):
    posts = Post.objects.all()
    filters = FiltersForms(request.GET, queryset=posts)
    posts = filters.qs
    page_number = request.GET.get('page')
    paginator = Paginator(posts, 2)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts':posts,'filters':filters,}
    return render(request,"OurProfile/posts.html",context)
@login_required(login_url='login')
def post(request,pk):
    post = Post.objects.get(id=pk)
    comments = CreateCommentForm()
    if request.method == 'POST':
        comments = CreateCommentForm(request.POST)
        if comments.is_valid():
            comments.instance.post_id = pk
            comments.instance.customer_comment = request.user
            comments.save()
        return redirect('post', post.id)
    context={'post':post, 'comments':comments}
    return render(request,"OurProfile/post.html",context)
@login_required(login_url='login')
def createpost(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if form.is_valid(): 
                form.instance.customer = request.user
                form.save() 
            return redirect('posts')
    context = {'form':form}
    return render(request,"OurProfile/create_post_form.html",context)
@login_required(login_url='login')
def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = CreatePostForm(instance=post)
    if request.user == post.customer:
        if request.method == 'POST':
            form = CreatePostForm(request.POST, request.FILES, instance=post)
            if request.user.is_authenticated:
                if form.is_valid(): 
                    form.instance.customer = request.user
                    form.save() 
                return redirect('posts')
            else:
                return HttpResponse("wrong....")
        context = {'form':form}
        return render(request,"OurProfile/update_post_form.html",context)
    else:
        return HttpResponse("你沒權！！")
@login_required(login_url='login')
def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    if request.user == post.customer:
        post.delete()
    else:
        return HttpResponse("你沒權！！")      
    return redirect('posts')
@unauthenticated_user
def createuser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render(request,"OurProfile/register_form.html",context)
@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Your password or account wrong!')
            return redirect('login')
    return render(request,"OurProfile/login_form.html")
def logout(request):
    django_logout(request)
    return render(request,"OurProfile/home.html")
@login_required(login_url='login')
def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('OurProfile/email_template.html',{
                        'name':request.POST['name'],
                        'email':request.POST['email'],
                        'message':request.POST['message'],
                        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            #from_email = request.POST['email'],
            ['d1094181301@gm.lhu.edu.tw']
            )
        email.fail_silently = False
        email.send()
    return HttpResponse('email was sent')
@login_required(login_url='login')
def changepassword(request):
    form = ChangePassword(request.user)
    if request.method == 'POST':
        form = ChangePassword(request.user,request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    context = {'form':form}
    return render(request,"OurProfile/changepassword.html",context)