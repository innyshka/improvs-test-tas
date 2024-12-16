# notes/admin.py
from django.contrib import admin

from apps.note.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'user', 'created_at', 'updated_at',
    list_filter = 'user', 'created_at',
    search_fields = 'title', 'content', 'user__username',
    ordering = '-created_at',
