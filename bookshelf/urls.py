from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail'),
    path('authors/<slug:slug>/', views.author_detail, name='author_detail'),
    path('genres/<slug:slug>/', views.genre_detail, name='genre_detail'),
]
