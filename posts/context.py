import random
from .models import Post,Category
def all_posts(request):
    posts=Post.objects.all().order_by('-created_date')
    all_posts=random.sample(list(posts),len(posts))
    return{'all_posts':all_posts}

def category_data(request):
    categories = Category.objects.all()
    category_data = {}

    for i in categories:
        category_data[i.category_name] = Post.objects.filter(category=i).count()

    return {'category_data': category_data}