from django.shortcuts import render
from .models import Post
from requests import request

# Create your views here.
def main_page(request):
    posts = Post.objects.all
    return render(request, 'main_page.html', {'posts': posts})