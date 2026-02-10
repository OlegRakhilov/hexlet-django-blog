from django.test import TestCase
from django.urls import reverse
from hexlet_django_blog.article.models import Article

class ArticlesTest(TestCase):
    fixtures = ['articles.json']

    def test_articles_list(self):
        response = self.client.get('/articles/')
        # Now this will be 5 because of the fixture!
        self.assertEqual(len(response.context['articles']), 5)

    
