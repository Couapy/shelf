from django.contrib.auth.models import User
from django.db import models


class Shelf(models.Model):
    """Shelf Model."""

    name = models.CharField(
        verbose_name="Nom",
        max_length=128,
    )
    slug = models.SlugField(
        verbose_name="Adresse (slug)",
        max_length=96,
    )
    description = models.TextField(
        verbose_name="Description"
    )

    @property
    def books(self):
        return Book.objects.filter(shelf=self)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book Model."""

    shelf = models.ForeignKey(
        verbose_name="Étagère",
        on_delete=models.CASCADE,
        to=Shelf,
        null=True,
    )
    name = models.CharField(
        verbose_name="Nom",
        max_length=128,
    )
    owner = models.ForeignKey(
        verbose_name="Auteur",
        on_delete=models.CASCADE,
        to=User,
        null=True,
    )
    slug = models.SlugField(
        verbose_name="Adresse (slug)",
        max_length=96,
    )
    description = models.TextField(
        verbose_name="Description"
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    modification_date = models.DateTimeField(
        auto_now=True,
        null=True,
    )

    @property
    def chapters(self):
        return Chapter.objects.filter(book=self)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    """Chapter model."""

    book = models.ForeignKey(
        verbose_name="Livre",
        on_delete=models.CASCADE,
        to=Book,
        null=True,
    )
    name = models.CharField(
        verbose_name="Nom",
        max_length=128,
    )
    owner = models.ForeignKey(
        verbose_name="Auteur",
        on_delete=models.CASCADE,
        to=User,
        null=True,
    )
    slug = models.SlugField(
        verbose_name="Adresse (slug)",
        max_length=96,
    )
    description = models.TextField(
        verbose_name="Description"
    )
    content = models.TextField(
        verbose_name="Contenu"
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    modification_date = models.DateTimeField(
        auto_now=True,
        null=True,
    )

    def __str__(self):
        return self.name