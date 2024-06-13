from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Publisher
import datetime


def home_page(request):
    context = {
        'title': 'Main page',
        'name': 'Djonas',
        'text': 'Hello!',
    }
    return render(request, 'home_page.html', context)


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s.</body></html>" % now
    return HttpResponse(html)


def authors(request):
    all_authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': all_authors})


def books(request):
    all_books = Book.objects.all()
    return render(request, 'books.html', {'books': all_books})


def publishers(request):
    all_publishers = Publisher.objects.all()
    return render(request, 'publishers.html', {'publishers': all_publishers})


def authors_books_information(request):
    selected_author = request.GET.get('author', None)
    books_info = []

    if selected_author:
        books = Book.objects.filter(author__name=selected_author)
        for book in books:
            books_info.append({
                'title': book.title,
                'publication_date': book.publication_date,
                'rating': book.rating,
            })
    else:
        books_info = [("No author selected",)]

    return render(request, 'authors_books_information.html', {'books_info': books_info})
