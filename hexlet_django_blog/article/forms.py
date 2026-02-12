from django import forms
from .models import Comment, Article

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # Указываем поля, которые пользователь будет заполнять при создании статьи
        fields = ['title', 'body'] 