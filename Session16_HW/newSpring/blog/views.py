from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Scrap
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.





def home(request):
    posts = Post.objects.all()
    return render(request, "main/home.html", {"posts": posts})


def detail(request):
    # post = Post.objects.get(pk=post_pk)
    posts = Post.objects.all()

    if request.method == "POST":
        content = request.POST["content"]
        # Comment.objects.create(post=post, content=content, author=request.user)

        return redirect("detail")
    return render(request, "main/detail.html", {"posts": posts})


@login_required(login_url="/registration/login")
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = Post.objects.create(
            title=title, content=content, author=request.user,
            )
        return redirect("detail")

    return render(request, "main/new.html")


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.filter(pk=post_pk).update(title=title, content=content)
        return redirect("detail", post_pk)

    return render(request, "edit.html", {"post": post})


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        found_user = User.objects.filter(username=username)
        if found_user:
            # error = "당신의 아이디는 이미 포위되었다. 다른 녀석을 가져와"
            error = "이미 있는 아이디다 -.-😎 다른 녀석을 가져와."
            return render(request, "registration/signup.html", {"error":error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect('home')
    return render(request, "registration/signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            return redirect(request.GET.get("next", "/"))
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, "registration/login.html", {"error":error})

    return render(request, "registration/login.html")

def logout(request):
    auth.logout(request)
    return redirect("home")



def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("detail", post_pk)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("home")
