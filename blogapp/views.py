from django.shortcuts import render,get_object_or_404
from blogapp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def hello(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blogapp/index.html',{'post_list':post_list})
def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,
                                                              publish__month=month,
                                                              publish__day=day)
    return render(request,'blogapp/post_detail.html',{'post':post})
from django.core.mail import send_mail
from blogapp.forms import EmailSendForm
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recommends you to read"{}"'.format(cd['name'],cd['email'],post.title)
            message='read post at:\n {}\n\n{}\'s comments:\n{}'.format('url',cd['name'],cd['comments'])
            send_mail(subject,message,'bishtpython@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'blogapp/mail.html',{'form':form,'post':post,'sent':sent})
