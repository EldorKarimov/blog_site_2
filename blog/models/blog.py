from django.db import models
from .tag import Tag
from .category import Category

from accounts.models import CustomUser
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = RichTextField()
    image = models.ImageField(upload_to='blog')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.PositiveBigIntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blog')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='blog')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title