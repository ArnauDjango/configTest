# blog/views.py

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogUpdateView(UpdateView):
    model = Post 
    template_name = 'blog/post_edit.html'
    fields = [
        'title',
        'body'
    ]

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = [
        'title',
        'body',
        'author'
    ]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')