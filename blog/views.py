from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-create_at')

    return render(request, 'blog/post_list.html', {'posts': posts})

