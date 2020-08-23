from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from mediumclone_core import models
from . import serializers

class TestEndpoint(APIView):
    def get(self, request):
        return Response({"status": "Succesfull!"})

class ArticlesEndpoint(generics.ListAPIView):
    queryset =  models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

