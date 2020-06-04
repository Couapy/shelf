from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name="index"),
    path('shelf/<slug:shelf_slug>/', views.shelf, name="shelf"),
    path('book/<slug:book_slug>/', views.book, name="book"),
    path('book/<slug:book_slug>/<slug:chapter_slug>/', views.chapter, name="chapter"),
]
