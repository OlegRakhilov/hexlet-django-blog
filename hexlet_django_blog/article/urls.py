from django.urls import path
from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.ArticleIndexView.as_view(), name='articles_index'),
    path("<int:id>/", views.ArticleIndexView.as_view(), name='article_detail'),
    path("<str:tags>/<int:article_id>/", views.ArticleIndexView.as_view(), name='article'),
]