from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Keyword(models.Model):
    name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Blog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    title = models.CharField(max_length=254)
    body = models.TextField(validators=[MinLengthValidator(20)])
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

'''
class Reply(models.Model):
    blog = models.ForeignKey(Blog, related_name='replies',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.name
'''