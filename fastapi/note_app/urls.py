from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', views.NoteRetrieveUpdateDestroyView.as_view(), name='note-detail'),
    path('tags/', views.TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag-detail'),
]
