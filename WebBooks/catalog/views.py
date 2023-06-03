from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookInstance, Status, Author, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_books_instance = BookInstance.objects.all().count()
    num_books_instance_available = BookInstance.objects.filter(status__exact=3).count()
    print(num_books_instance_available)
    num_authors = Author.objects.all().count()
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_books_instance': num_books_instance,
            'num_books_instance_available': num_books_instance_available,
            'num_authors': num_authors
            }
    )

