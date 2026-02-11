from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import Article, Comment
from .forms import ArticleCommentForm  
from django.contrib import messages


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        
        # Получаем все комментарии для этой статьи
        comments = article.comment_set.all() 
        
        return render(
            request,
            "articles/article.html",
            context={
                "article": article,
                "comments": comments, # Передаем в шаблон
            },
        )

class ArticleCommentsView(View):
    # Параметры приходят в kwargs
    def get(self, request, *args, **kwargs):
        # Извлекаем значения по именам из маршрута
        article_id = kwargs.get('article_id')
        comment_id = kwargs.get('id')

        # Теперь мы можем использовать их для поиска в БД
        article = get_object_or_404(Article, id=article_id)
        comment = get_object_or_404(Comment, id=comment_id, article=article)

        return render(request, 'articles/comments/article.html', context={
            'article': article,
            'comment': comment,
        })

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
    
class ArticleCommentFormView(View):
    def post(self, request, *args, **kwargs):
        # 1. Находим статью, к которой пишем коммент
        article = get_object_or_404(Article, id=kwargs['article_id'])
        form = ArticleCommentForm(request.POST)
        
        if form.is_valid():
            # 2. Создаем объект, но не сохраняем в БД сразу (commit=False)
            comment = form.save(commit=False)
            # 3. Привязываем статью к комменту
            comment.article = article
            # 4. Вот теперь сохраняем
            comment.save()
            messages.success(request, 'Комментарий успешно добавлен!')
            return redirect('article_detail', id=article.id)
        
        messages.error(request, 'Ошибка при добавлении комментария.')
        return render(request, 'articles/comment_form.html', {'form': form, 'article': article})

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        form = ArticleCommentForm()
        return render(request, 'articles/comment_form.html', {'form': form, 'article': article})