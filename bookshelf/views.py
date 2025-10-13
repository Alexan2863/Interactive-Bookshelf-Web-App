from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Genre


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'bookshelf/book_detail.html', {'book': book})


def author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    return render(request, 'bookshelf/author_detail.html', {'author': author})


def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    return render(request, 'bookshelf/genre_detail.html', {'genre': genre})
