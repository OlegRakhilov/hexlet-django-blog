from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import Article, Comment
from .forms import ArticleCommentForm, ArticleForm  
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
    
class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        # Создаем пустой экземпляр формы
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # Наполняем форму данными из запроса
        form = ArticleForm(request.POST)
        if form.is_valid():
            # Если всё ок — сохраняем в БД
            form.save()
            # Добавляем сообщение об успехе
            messages.success(request, 'Статья успешно создана!')
            # Редирект на список всех статей
            return redirect('articles_index')
        
        # Если в форме ошибки, возвращаем её пользователю (с подсветкой ошибок)
        return render(request, 'articles/create.html', {'form': form})
    
class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles_index")

        return render(
        request, "articles/update.html", {"form": form, "article_id": article_id}
        )