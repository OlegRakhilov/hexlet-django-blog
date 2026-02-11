from django import forms
from .models import Comment

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]