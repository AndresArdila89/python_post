from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

def index(request):
    return render(request, 'posts/index.html',{'posts': Post.objects.all(),'title': Post.objects.last()})
