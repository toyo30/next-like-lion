from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
import datetime
# Create your views here.

def list_page(request):
    posts = Post.objects.all()
    return render(request, 'app/list_page.html', {
        'posts':posts,
    })

def create_page(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('list_page')
    return render(request, 'app/create_page.html')


def detail_page(request, post_pk):
    detail_data = get_object_or_404(Post, pk = post_pk)
    post = Post.objects.get(pk=post_pk)
    #조회수 기능 (쿠키 이용)

    response =  render(request, 'app/detail_page.html', {'post':post})

    expire_date, now = datetime.datetime.now(), datetime.datetime.now()
    expire_date += datetime.timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get('hitblog', '_')

    if f'_{post_pk}_' not in cookie_value:
        cookie_value += f'{post_pk}_'
        response.set_cookie('hitblog', value=cookie_value, max_age=max_age, httponly=True)
        detail_data.hit += 1
        detail_data.save()
    return response
#get과 filter의 차이는 무엇일까요?
#get은 하나의 객체가 반환됩니다. 
#filter는 조건에 해당하는 객체를 담은 쿼리셋이 반환됩니다.


def edit_page(request, post_pk):
    post = Post.objects.filter(pk=post_pk)

    if request.method == "POST":
        post.update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('detail_page', post_pk)
    return render(request, 'app/edit_page.html', {'post':post[0]})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('list_page')