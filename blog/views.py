from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post


def say_hello(request):
    return HttpResponse('HelloWorld')

def output_gif(request):
    return HttpResponse('No idea how to get a gif')
def image_show(request):
    return HttpResponse('No idea how to get an image')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})