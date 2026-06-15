from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .forms import RegistrationForm,LoginForm,EditProfileForm,EditUserForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Profile
from django.shortcuts import render, get_object_or_404
from posts.models import Post,Category
class reverse_urls:
    def homeurl():
        return reverse('home')
    def loginurl():
        return reverse('login')
    def profileurl(request):
        return reverse('profile',args=[request.user.id])
    def categoryurl(request):
        return reverse('category',args=[request.category.category_name])
    def singleurl(id):
        return reverse('single',args=[id])
    




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(owner=user)
            login(request, user)
            return HttpResponseRedirect(reverse_urls.homeurl())
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})




def user_login(request):
    if request.method=='POST':
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse_urls.homeurl())
    else:
        form=LoginForm()
    return render(request,'accounts/user_login.html',{'form':form})


def edit_profile(request,id):
    user = request.user
    try:
        profile = Profile.objects.get(owner=user)
    except Profile.DoesNotExist:
        profile=None
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile=profile_form.save(commit=False)
            if profile.owner_id is None:
                profile.owner=request.user

            profile_form.save()
            return HttpResponseRedirect(reverse_urls.profileurl(request))
    else:
        user_form = EditUserForm(instance=user)
        profile_form = EditProfileForm(instance=profile)

    return render(
        request,'accounts/edit_profile.html',{'user_form': user_form,'profile_form': profile_form})




def profile(request, id):
    profile_user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(author=profile_user)
    try:
        profile = Profile.objects.get(owner=profile_user)
    except Profile.DoesNotExist:
        profile = None
    return render(request,'blog.html',{'profile_user': profile_user,'posts': posts,'profile': profile,})




def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_urls.homeurl())
