from django.shortcuts import render
from blogapp.models import Post

# Create your views here.
def hello(request):
    post_list=Post.objects.all()
    return render(request,'blogapp/index.html',{'post_list':post_list})
