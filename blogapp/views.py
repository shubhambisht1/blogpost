from django.shortcuts import render,get_object_or_404
from blogapp.models import Post

# Create your views here.
def hello(request):
    post_list=Post.objects.all()
    return render(request,'blogapp/index.html',{'post_list':post_list})
def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,
                                                              publish__month=month,
                                                              publish__day=day)
    return render(request,'blogapp/post_detail.html',{'post':post})
