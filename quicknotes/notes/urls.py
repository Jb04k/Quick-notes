# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
]
