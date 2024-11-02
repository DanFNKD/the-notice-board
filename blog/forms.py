from .models import Post, Comment, UserProfile
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5, "placeholder": "Write your post here..."}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Add your comment',
        }
        widgets = {
            'body': forms.Textarea()
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location']