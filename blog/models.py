from django.db import models
from django.conf import settings
from django.utils import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=True, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True, verbose_name='Date Published')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    image = models.ImageField(upload_to=media, null=False, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title
    