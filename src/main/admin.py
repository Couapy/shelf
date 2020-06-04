from django.contrib import admin

from .models import Shelf, Book, Chapter

admin.site.register(Shelf)
admin.site.register(Book)
admin.site.register(Chapter)
