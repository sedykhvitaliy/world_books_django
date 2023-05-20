from django.contrib import admin
from .models import Genre, Language, Author, Book, BookInstance, Status

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Author, AuthorAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        (
            'Экземпляр книги', {'fields': ('book', 'imprint', 'barcode')}
        ),
        (
            'Статус и окончание его действия', {'fields': ('status', 'due_back')}
        ),
    )


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]
