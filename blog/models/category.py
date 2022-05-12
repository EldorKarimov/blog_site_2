from django.db import models

from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='category')
    description = models.TextField()
    user = models.ManyToManyField(CustomUser, related_name='category')

    def __str__(self):
        return self.name