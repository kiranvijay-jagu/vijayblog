from django import forms
from .models import Post,Comment
class Post_creation_form(forms.ModelForm):
    class Meta:
        model=Post
        fields=['post_title','post_content','post_image','category']

