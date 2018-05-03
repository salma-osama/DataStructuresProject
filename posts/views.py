from django.shortcuts import render,redirect
from .models import Post , Friend
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/accounts/login/")
def timeline(request):
    posts =Post.objects.all().order_by('date')
    user=request.user
    users=User.objects.exclude(id=request.user.id)
    friend=Friend.objects.get(current_user=request.user)
    friends=friend.users.all()
    #arg={'myName':user}
    args={'posts':posts , 'users':users , 'friends':friends}
    return render(request,'posts/timeline.html',args)

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
def change_friends(request,operation,pk):
    new_friend=User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user,new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user,new_friend)
    return redirect('posts:timeline')

