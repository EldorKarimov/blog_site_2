from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True,
    help_text = (
                    "50 ta belgidan iborat username kiritishingiz mumkin."
                ),
    error_messages = {
                    "unique": "Bunaqa user avval ruyxatdan utgan.",
                    },
    )
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='accounts')
    addres = models.CharField(max_length=100, null=True, blank=True)


    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
