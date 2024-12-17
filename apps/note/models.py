from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.CharField(max_length=510, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name="Дата та час створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата та час оновлення")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created_at"]

