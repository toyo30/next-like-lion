from turtle import title
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    posts = Post.objects.all()

    return render(request, "app/home.html", {"posts": posts})


@login_required(login_url="/registration/login")
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = Post.objects.create(title=title, content=content, author=request.user)
        return redirect("detail", new_post.pk)

    return render(request, "app/new.html")


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.filter(pk=post_pk).update(title=title, content=content)
        return redirect("detail", post_pk)

    return render(request, "app/edit.html", {"post": post})


@login_required(login_url="/registration/login")
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    #유저 정보 담기
    print(type(post.author), "post.author")
    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(post=post, content=content, author=request.user)

        return redirect("detail", post_pk)
    return render(request, "app/detail.html", {"post": post})


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("detail", post_pk)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("home")

def signup(request):
  if request.method=="POST":
    username = request.POST["username"]
    password = request.POST["password"]

    found_user = User.objects.filter(username=username)
    if len(found_user):
      error="이미 아이디가 존재합니다"
      return render(request, "app/registration/signup.html", {"error": error})
    
    new_user = User.objects.create_user(username=username, password=password)
    auth.login(request, new_user) #유저정보를 세션에 저장한다는 함수.
                                  #만약 세션에 저장해주지 않는다면,
                                  #페이지를 이동할 때마다 다시 로그인 해줘야 함.
    return redirect("home")
  return render(request, "app/registration/signup.html")

def login(request):
  if request.method =="POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(
        request, 
        user, 
        backend="django.contrib.auth.backends.ModelBackend" 
        #user 정보를 어느 백엔드에서 가져와야 할지를 설명해줌, 에러를 미연에 방지할 수 있다
      ) 

      # return redirect("home")
      return redirect(request.GET.get("next", "/")) #단순히 home으로 돌아가는 것이 아니라, 이전 페이지로 돌아갈 수 있도록 함!

    error ="아이디 또는 비밀번호가 틀립니다"
    return render(request, "app/registration/login.html", {"error":error})
  
  return render(request, "app/registration/login.html")


def logout(request):
  auth.logout(request)
  return redirect("home")