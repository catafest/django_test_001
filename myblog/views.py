from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('create_date')
    return render(request, 'myblog/post_list.html', {'posts':posts})
def about(request):
    return render(request, 'about.html', {})
