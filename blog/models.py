from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Keyword(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Blog(models.Model):
    slug = models.SlugField(max_length=254, unique=True, db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    keyword = models.ManyToManyField(Keyword, blank=True)
    title = models.CharField(max_length=254)
    body = models.TextField(validators=[MinLengthValidator(20)])
    image_url = models.URLField(max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

