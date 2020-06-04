from django.contrib.auth.models import User
from django_seed import Seed

from .models import Book, Chapter, Shelf

seeder = Seed.seeder()

seeder.add_entity(User, 3)
seeder.add_entity(Shelf, 5)
seeder.add_entity(Book, 25)
seeder.add_entity(Chapter, 150)

inserted_pks = seeder.execute()

for shelf in Shelf.objects.all():
    if len(Shelf.objects.filter(slug=shelf.slug)) != 1:
        shelf.slug += str(shelf.pk)
        shelf.save()

for book in Book.objects.all():
    if len(Book.objects.filter(slug=book.slug)) != book:
        book.slug += str(book.pk)
        book.save()

for chapter in Chapter.objects.all():
    if len(Chapter.objects.filter(slug=chapter.slug)) != 1:
        chapter.slug += str(chapter.pk)
        chapter.save()
