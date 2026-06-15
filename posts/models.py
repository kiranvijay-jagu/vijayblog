from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    category_name=models.CharField(max_length=50)
    def __str__(self):
        return self.category_name
    
class Post(models.Model):
    post_title=models.CharField(max_length=50)
    post_content=models.TextField()
    post_image=models.FileField(upload_to='posts/')
    created_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.post_title

class Comment(models.Model):
    comment_message=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
