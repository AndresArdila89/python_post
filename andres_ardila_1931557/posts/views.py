from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post



# Create your views here.

def index(request):
    return render(request, 'posts/index.html',{'posts': Post.objects.all(),'title': Post.objects.last()})

def details(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,'posts/details.html',{'post': post})
