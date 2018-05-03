from django.shortcuts import render,redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/accounts/login/")
def timeline(request):
    posts =Post.objects.all().order_by('date')
    user=request.user
    arg={'myName':user}
    return render(request,'posts/timeline.html',{'posts':posts})

# def user_profile(request,slug):
#     return HttpResponse(slug)

@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method=='POST':
        form=forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            #save article to the database
            instance=form.save(commit=False)
            #now we have an instance of the article that has been created
            #we'll attach the user who is logged in to it
            instance.author=request.user
            instance.save()
            return redirect('posts:timeline')
    else:
        form=forms.CreatePost()
    return render(request,'posts/post_create.html',{'form':form.as_p })
# @login_required(login_url="/accounts/login/")
# def post_like(request):
#     user=form.save()
#     addLike(request,user)
