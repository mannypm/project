from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('us/', views.us, name='us'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<str:code>/', views.delete_book, name='delete_book'),
    path('edit_book/<str:code>/', views.edit_book, name='edit_book'),
    path('book_edition_done/', views.book_edition_done, name='book_edition_done'),
]