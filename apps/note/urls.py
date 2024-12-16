from django.urls import path

from apps.note import views

urlpatterns = [
    path('create/', views.NoteCreateAPIView.as_view(), name='note-create'),
    path('update/<int:pk>/', views.NoteUpdateAPIView.as_view(), name='note-update'),
    path('delete/<int:pk>/', views.NoteDeleteAPIView.as_view(), name='note-delete'),
    path('detail/<int:pk>/', views.NoteDetailAPIView.as_view(), name='note-detail'),
    path('', views.NoteListAPIView.as_view(), name='note-list'),
]