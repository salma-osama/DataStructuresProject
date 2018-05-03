from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import RegisterationForm ,EditProfileForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash

def signup_view(request):
    if request.method =='POST':
        # form = UserCreationForm(request.POST)
        form=RegisterationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(reverse('posts:timeline'))
    else:
        form=RegisterationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:timeline')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form.as_p})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

@login_required(login_url="/accounts/login/")
def view_profile(request):
    user = request.user
    args={'myname':user}
    return render(request,'accounts/profile.html',args)

@login_required(login_url="/accounts/login/")
def view_my_profile(request):
    args={'user':request.user}
    return render(request,'accounts/my_profile.html',args)

@login_required(login_url="/accounts/login/")
def edit_my_profile(request):
    if request.method=='POST':
        form =EditProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('accounts:my_profile')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request,'accounts/edit_my_profile.html',{'form':form})


@login_required(login_url="/accounts/login/")
def edit_my_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:my_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

@login_required(login_url="/accounts/login/")
def view_me(request):
    args={'user':request.user}
    return render(request,'accounts/about_me.html',args)
