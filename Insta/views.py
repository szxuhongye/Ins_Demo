from django.views.generic import TemplateView, ListView
from Insta.models import Post
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HellowWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    template_name = 'post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
