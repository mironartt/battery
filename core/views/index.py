from django.conf import settings
from django.views import generic
from django.shortcuts import render, redirect, render_to_response, get_object_or_404

from ..models.globals import BlogPost, Images

class IndexViewExample(generic.View):

    def get(self, request, *args, **kwargs):
        context = {
            'test':'ZAEBUMBA!!!!!!!!!!!!!!!'
        }

        return render(request, 'index_example.html', context)



class IndexView(generic.View):

    def get(self, request, *args, **kwargs):
        context = {
            'test':'ZAEBUMBA!!!!!!!!!!!!!!!'
        }

        return render(request, 'index.html', context)

class BlobView(generic.View):

    def get(self, request, *args, **kwargs):
        context = {
        'posts': BlogPost.objects.filter(availavled=True)
        }

        return render(request, 'blog_index.html', context)

class BlogPageView(generic.View):

    def get(self, request, *args, **kwargs):

        post = BlogPost.objects.get(id=kwargs.get('pk'))
        context = {
            'post': post,
        }

        return render(request, 'blob_page.html', context)