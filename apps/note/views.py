from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache

from apps.note.models import Note
from apps.note.serializers import NoteSerializer
from apps.note.utils.func import get_queryset_with_cache


class NoteListAPIView(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return get_queryset_with_cache(self.request.user)


class NoteCreateAPIView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = IsAuthenticated,

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        cache.delete(f"user_notes_{user.id}")


class NoteUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NoteSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.delete(f"user_notes_{self.request.user.id}")


class NoteDeleteAPIView(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.delete(f"user_notes_{self.request.user.id}")


class NoteDetailAPIView(generics.RetrieveAPIView):
    serializer_class = NoteSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return get_queryset_with_cache(self.request.user)
