from django.db import models


# Create your models here.
class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email
