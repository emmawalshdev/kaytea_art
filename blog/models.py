from django.db import models
from django.core.validators import MinLengthValidator

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Keyword(models.Model):
    name = models.CharField(max_length=80)
    friendly_name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Blog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User, null=True, blank=True,
                               on_delete=models.CASCADE)
    teaser = RichTextField(validators=[MinLengthValidator(70)])
    body = RichTextField(validators=[MinLengthValidator(70)])
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Reply(models.Model):
    blog = models.ForeignKey(Blog, related_name='replies',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, blank=True,
                               on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=600)

    def __str__(self):
        return self.body
