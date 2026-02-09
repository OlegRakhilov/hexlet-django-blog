from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ["title", "body"]
    list_filter = ['created_at']


admin.site.register(Article, ArticleAdmin)