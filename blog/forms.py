from .models import Post, Comment, UserProfile, Tag
from django import forms


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple,
        required=True
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'excerpt', 'tags']
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5, "placeholder":
                                      "Write your post here..."}),
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
