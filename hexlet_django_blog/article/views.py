from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class ArticleIndexView(View):
    def get(self, request, tags=None, article_id=None, *args, **kwargs):
        if tags and article_id:
            return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
        
        # Логика для обычного списка /articles/
        return render(request, 'articles/index.html', context={'articles': []})
