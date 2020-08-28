from django.urls import path
from . import views

urlpatterns = [
    path('test', views.TestEndpoint.as_view()),
    path('articles', views.ArticlesEndpoint.as_view(), name='articles'),
]
