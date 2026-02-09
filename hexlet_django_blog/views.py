from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from hexlet_django_blog.article.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', context={
        'articles': articles,
        'app_name': 'Articles' # Чтобы заголовок в шаблоне не был пустым
    })
    
def about(request):
    tags = ['обучение', 'python', 'django']
    # Передаем словарь (context) третьим аргументом
    return render(request, 'about.html', {'tags': tags})