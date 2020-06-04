from django.shortcuts import render

from .models import Book, Chapter, Shelf


def index(request):
    """Home view."""
    context = {
        'shelves': Shelf.objects.all(),
    }
    return render(request, 'main/list.html', context)


def shelf(request, shelf_slug):
    """Shelf view."""
    shelf = Shelf.objects.get(slug=shelf_slug)
    context = {
        'shelf': shelf,
    }
    return render(request, 'main/shelf.html', context)


def book(request, book_slug):
    """Book view."""
    book = Book.objects.get(slug=book_slug)
    context = {
        'book': book,
    }
    return render(request, 'main/book.html', context)


def chapter(request, book_slug, chapter_slug):
    """Chapter view."""
    book = Book.objects.get(slug=book_slug)
    chapter = Chapter.objects.get(slug=chapter_slug)
    context = {
        'book': book,
        'chapter': chapter,
    }
    return render(request, 'main/chapter.html', context)
