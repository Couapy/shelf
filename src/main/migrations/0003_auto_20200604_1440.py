# Generated by Django 3.0.4 on 2020-06-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=96, unique=True, verbose_name='Adresse (slug)'),
        ),
    ]
