from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Article
from hexlet_django_blog.article.models import Article

class ArticleIndexView(View):
    def get(self, request, id=None, *args, **kwargs):
        if id:
            article = get_object_or_404(Article, id=id)
            return render(request, 'articles/article.html', context={'article': article})
        
        
        # Логика для обычного списка /articles/
        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={'articles': articles})

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )