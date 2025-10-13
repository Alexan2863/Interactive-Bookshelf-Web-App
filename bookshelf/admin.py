from django.contrib import admin
from .models import Author, Genre, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    fields = ['title', 'slug', 'published_date']
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'bio']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BookInline]


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'slug']
    list_filter = ['published_date', 'author', 'genres']
    search_fields = ['title', 'summary', 'author__name']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['genres']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
