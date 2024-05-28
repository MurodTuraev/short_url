import string
import random
import uuid

from django.db import models

# Create your models here.

class URL(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=10, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.shortened_url:
            self.shortened_url = self.generate_shortened_url()
            self.clicks += 1
        super().save(*args, **kwargs)

    def generate_shortened_url(self):
        if self.shortened_url:
           return self.shortened_url
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(10))
        while URL.objects.filter(original_url=short_url).exists():
            short_url = ''.join(random.choice(characters) for _ in range(10))
        return short_url

    def __str__(self):
        return self.original_url

    class Meta:
        verbose_name = 'Shortened URL'
        verbose_name_plural = 'Shortened URLS'