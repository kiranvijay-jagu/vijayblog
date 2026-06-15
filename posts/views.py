from django.shortcuts import render
from . models import Post,Comment
from .forms import Post_creation_form
from accounts.views import reverse_urls
import random
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q
from accounts.models import Profile
    


def home(request):
        #all the variables those are sent to index template
    all_posts=Post.objects.all().order_by('-created_date')
    
    #category wise posta
    business_posts=Post.objects.filter(category__category_name='business').order_by('-created_date')
    culture_posts=Post.objects.filter(category__category_name='culture').order_by('-created_date')
    travel_posts=Post.objects.filter(category__category_name='travel').order_by('-created_date')
    political_posts=Post.objects.filter(category__category_name='politics').order_by('-created_date')




    #all random posts
    random_posts=random.sample(list(all_posts),len(all_posts))
    all_random_posts=random.sample(list(all_posts),len(all_posts))
    business_random=random.sample(list(business_posts),len(business_posts))
    culture_random=random.sample(list(culture_posts),len(culture_posts))
    travel_random=random.sample(list(travel_posts),len(travel_posts))
    travel_random1=random.sample(list(travel_posts),len(travel_posts))
    travel_random2=random.sample(list(travel_posts),len(travel_posts))

        #all the variables those are sent to index template


    return render(request,'index.html',{
        
        'business_posts':business_posts,
        'culture_posts':culture_posts,
        'travel_posts':travel_posts,
        'political_posts':political_posts,
        'all_random_posts':all_random_posts,
        'business_random':business_random,
        'culture_random':culture_random,
        'travel_random':travel_random,
        'travel_random1':travel_random1,
        'travel_random2':travel_random2,
        'travel_random':travel_random,
        
        })

def create_post(request):
    if request.method=='POST':
        form=Post_creation_form(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return HttpResponseRedirect(reverse_urls.profileurl(request))
    else:
        form=Post_creation_form()
    return render(request,'posts/create_post.html',{'form':form})



def single_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST' and request.user.is_authenticated:
        message = request.POST.get('message')
        Comment.objects.create(comment_message=message,post=post,author=request.user)
        return HttpResponseRedirect(reverse_urls.singleurl(id))
    comments = Comment.objects.filter(post=post)
    return render(request,'single.html',{'post': post,'comments': comments,'comments_count': comments.count()})



def category(request,category_name):
    business_posts=Post.objects.filter(category__category_name='business').order_by('-created_date')
    culture_posts=Post.objects.filter(category__category_name='culture').order_by('-created_date')
    travel_posts=Post.objects.filter(category__category_name='travel').order_by('-created_date')
    political_posts=Post.objects.filter(category__category_name='politics').order_by('-created_date')
    category_wise_posts={'business':business_posts,'culture':culture_posts,'travel':travel_posts,'politics':political_posts}
    if category_name in category_wise_posts.keys():
        return render(request,'category.html',{'category_name':category_name,'category_wise_posts':category_wise_posts[category_name]})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.post_image:
        post.post_image.delete(save=False)
    post.delete()
    return HttpResponseRedirect(reverse_urls.profileurl(request))



def search_result(request):
    print(request.GET)
    keyword=request.GET.get('keyword')
    print(keyword)
    searched_posts=Post.objects.filter(Q(post_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
    return render(request,'search-result.html',{'searched_posts':searched_posts,'keyword':keyword})

