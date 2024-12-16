from django.core.cache import cache

from apps.note.models import Note


def get_queryset_with_cache(user):
    notes = cache.get(f"user_notes_{user.id}")
    if not notes:
        notes = Note.objects.filter(user=user)
        cache.set(f"user_notes_{user.id}", notes, timeout=60 * 10)
    return notes