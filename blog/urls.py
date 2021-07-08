from django.urls import path
from . import views 

urlpatterns = [
    path('articles/', views.list, name="list"),
    path('article/<int:article_id>', views.article, name="article")
]