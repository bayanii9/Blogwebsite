from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

from .models import Category, Comment, Post


def home(request):
    posts = Post.objects.select_related('author', 'category')[:5]
    return render(request, 'blog/main.html', {'posts': posts})


def users_list(request):
    users = get_user_model().objects.order_by('username')
    return render(request, 'blog/users.html', {'users': users})


def posts_list(request):
    posts = Post.objects.select_related('author', 'category')
    return render(request, 'blog/blogs.html', {'posts': posts})


def comments_list(request):
    comments = Comment.objects.select_related('post', 'user')
    return render(request, 'blog/comments.html', {'comments': comments})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})


def post_detail(request, slug):
    post = get_object_or_404(
        Post.objects.select_related('author', 'category'),
        slug=slug,
    )
    comments = post.comments.select_related('user')
    return render(
        request,
        'blog/blogdetails.html',
        {'post': post, 'comments': comments},
    )