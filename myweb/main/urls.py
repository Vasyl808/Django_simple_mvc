from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path("create-article", views.create_article, name="create-article"),
    path("articles", views.get_articles, name='articles'),
    path('article/<int:id>', views.get_article, name='article'),
    path('article/<int:id>/delete', views.delete_article, name='article_delete'),
    path('article/<int:id>/update', views.update_article, name='article_update')
]
