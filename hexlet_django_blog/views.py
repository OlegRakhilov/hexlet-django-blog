from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse

def index(request):
    # Вместо отрисовки шаблона делаем редирект
    return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))
    
def about(request):
    tags = ['обучение', 'python', 'django']
    # Передаем словарь (context) третьим аргументом
    return render(request, 'about.html', {'tags': tags})