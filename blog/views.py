from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('HelloWorld')

def output_gif(request):
    return HttpResponse('No idea how to get a gif')
def image_show(request):
    return HttpResponse('No idea how to get an image')
def post_list(request):
    return render(request, 'blog/post_list.html', {})