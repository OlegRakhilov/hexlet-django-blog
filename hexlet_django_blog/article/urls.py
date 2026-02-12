from django.urls import path
from hexlet_django_blog.article import views

from hexlet_django_blog.article.views import IndexView

urlpatterns = [
    path("", views.IndexView.as_view(), name='articles_index'),
    path("comment/", views.ArticleCommentFormView.as_view(), name='articles_comment_create'),
    path('create/', views.ArticleCreateView.as_view(), name='articles_create'),
    path("<int:id>/", views.ArticleView.as_view(), name='article_detail'),
    path("<str:tags>/<int:article_id>/", views.ArticleView.as_view(), name='article'),
    path("<int:article_id>/comment/", views.ArticleCommentFormView.as_view(), name='articles_comment_create'),
]