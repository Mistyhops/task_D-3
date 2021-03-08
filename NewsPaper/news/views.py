from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-time')


class PostDetail(DetailView):
    model = Post
    template_name = 'specificnews.html'
    context_object_name = 'specificnews'
