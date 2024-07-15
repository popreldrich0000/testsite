from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from .forms import post_form

def say_hello(request):
    return HttpResponse('HelloWorld')

def output_gif(request):
    return HttpResponse('No idea how to get a gif')
def image_show(request):
    return HttpResponse('No idea how to get an image')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
def create_view(request):
    context = {}
    form = post_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] =  form
    return render(request, "blog/create_view.html", context) 
def list_view(request):
    context = {}
    context["dataset"] = Post.objects.all()
    return render(request , "blog/list_view.html",context)
def detail_view(request,id):
    context={}
    context["data"] = Post.objects.get(id=id)
    return render(request,"blog/detail_view.html", context)
def update_view(request, id):
    context  = {}
    obj = get_object_or_404(Post, id = id)
    form  = post_form(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"] = form
    return render(request , "blog/update_view.html" , context)
def delete_view(request, id):
    context ={}
    obj = get_object_or_404(Post, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "blog/delete_view.html", context)

