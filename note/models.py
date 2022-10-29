from datetime import datetime
from django.db import models
from django.urls import reverse_lazy

from user.models import UserModel


class NoteModel(models.Model):
    title = models.CharField(
        max_length=100
    )

    content = models.TextField()

    time_create = models.TextField(
        default=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse_lazy('user:profile')
