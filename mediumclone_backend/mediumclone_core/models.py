from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

