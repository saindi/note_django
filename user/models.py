from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    email = models.EmailField(
        unique=True
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "користувач"
        verbose_name_plural = "користувачі"

