from rest_framework import serializers
from mediumclone_core import models

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


