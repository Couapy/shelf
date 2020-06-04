# Generated by Django 3.0.4 on 2020-05-21 17:34

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField(blank=True, help_text='300 caractères maximum.', max_length=300, null=True, verbose_name='Biographie')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Site web')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=accounts.models.user_directory_path, verbose_name='Photo de profil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
