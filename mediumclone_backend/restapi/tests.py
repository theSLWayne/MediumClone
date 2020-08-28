from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from mediumclone_core import models
from restapi import serializers

class ArticleTests(APITestCase):
    def test_getArticles(self):
        # first create some instances of article
        for i in range(10):
            models.Article.objects.create(
                title=f'article {i} title',
                subtitle=f'article {i} subtitle',
                content=f'article {i} content',
                featured_image=f'article {i} img path'
            )

        # make an API request and get the response
        url = reverse('articles')
        response = self.client.get(url, format='json')

        # also get articles directly from the DB
        articlesFromDatabase = models.Article.objects.all()
        articlesFromDatabase_json = serializers.ArticleSerializer(articlesFromDatabase, many=True)

        # compare the articles from DB, to articles from API response
        self.assertEqual(response.data, articlesFromDatabase_json.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


