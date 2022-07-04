from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Scrap
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.



def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if (request.method == 'POST'):
        Comment.objects.create(
            post=post,
            content=request.POST['content'],
            author=request.user
        )
        return redirect('detail', post_pk)

    existing_scrap = Scrap.objects.filter(
        post = Post.objects.get(pk=post_pk),
        user = request.user
    )

    existing_like = Like.objects.filter(
        post = Post.objects.get(pk=post_pk),
        user = request.user
    )
    if existing_like.count() > 0:
        existing_like_status = 1
    else:
        existing_like_status = 0

    existing_scrap = Scrap.objects.filter(
        post = Post.objects.get(pk=post_pk),
        user = request.user
    )
    if existing_scrap.count() > 0:
        existing_scrap_status = 1
    else:
        existing_scrap_status = 0

    return render(request, 'detail.html', {
        'post': post,
        'existing_like': existing_like,
        'existing_scrap': existing_scrap,
    })


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})

        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')

    return render(request, 'registration/signup.html')


def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))
    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='/registration/login')
def mypage(request):
    posts = Post.objects.all()


    user_likes = Like.objects.filter(
        user = request.user,
    )

    user_scraps = Scrap.objects.filter(
        user = request.user,
    )
    
    return render(request, 'mypage.html', { 
        "posts":posts,
        "user_likes":user_likes,
        "user_scraps":user_scraps,
    })


@csrf_exempt
def like(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        post_pk = request_body["post_pk"]

        existing_like = Like.objects.filter(
            post = Post.objects.get(pk=post_pk),
            user = request.user
        )
        if existing_like.count() > 0:
            existing_like.delete()
        else:
            Like.objects.create(
                post = Post.objects.get(pk=post_pk),
                user = request.user
            )
    post_likes = Like.objects.filter(
        post = Post.objects.get(pk=post_pk),
    )

    existing_like = Like.objects.filter(
        post = Post.objects.get(pk=post_pk),
        user = request.user
    )

    if existing_like.count() > 0:
        existing_like_status = 1
    else:
        existing_like_status = 0

    response = {
        'like_count' : post_likes.count(),
        'like_status': existing_like_status,
    }
    
    return HttpResponse(json.dumps(response))


@csrf_exempt
def scrap(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        print(request_body)
        post_pk = request_body["post_pk"]

        existing_scrap = Scrap.objects.filter(
            post = Post.objects.get(pk=post_pk),
            user = request.user
        )
        if existing_scrap.count() > 0:
            existing_scrap.delete()
        else:
            Scrap.objects.create(
                post = Post.objects.get(pk=post_pk),
                user = request.user
            )
    post_scraps = Scrap.objects.filter(
        post = Post.objects.get(pk=post_pk),
    )
    
    existing_scrap = Scrap.objects.filter(
        post = Post.objects.get(pk=post_pk),
        user = request.user
    )
    
    if existing_scrap.count() > 0:
        existing_scrap_status = 1
    else:
        existing_scrap_status = 0


    response = {
        'scrap_count' : post_scraps.count(),
        'scrap_status': existing_scrap_status,
    }
    
    return HttpResponse(json.dumps(response))