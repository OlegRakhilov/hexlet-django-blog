from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model): # Добавьте этот класс
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
