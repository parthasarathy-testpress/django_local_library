from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)


class AuthorInstanceInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorInstanceInline]



class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0   

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'summary', 'isbn', 'genre')
        }),
        ('Availability', {
            'fields': ('language',)
        }),
    )
    list_filter = ('author', 'genre', 'language')
    search_fields = ['title', 'author__last_name']
    ordering = ['title']
    inlines = [BooksInstanceInline]



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'imprint')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )