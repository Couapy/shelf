from django.shortcuts import render
from django.core.paginator import Paginator

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
    paginator = Paginator(book.chapters, 1)
    index = list(paginator.object_list).index(chapter) + 1
    page = paginator.page(index)

    try:
        previous_chapter = paginator.object_list[index-2]
    except Exception:
        previous_chapter = None
    try:
        next_chapter = paginator.object_list[index]
    except Exception:
        next_chapter = None

    return render(request, 'main/chapter.html', locals())
