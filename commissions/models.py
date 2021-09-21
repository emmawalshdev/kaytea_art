from django.db import models

SIZE_CHOICES = (
    ('', 'Canvas size *'),
    ('A5', 'A5'),
    ('A4', 'A4'),
    ('A2', 'A2'),
    ('A1', 'A1'),
    ('Not sure', 'Not sure'),
)

PET_NUM_CHOICES = (
    ('', 'Number of Pets *'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

MEDIA_CHOICES = (
    ('', 'Media Preference *'),
    ('penil', 'Pencil'),
    ('Acrylic', 'Acrylic'),
    ('Watercolor', 'Watercolor'),
    ('Not sure', 'Not sure'),
)


# Create your models here.
class Commissions(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, null=False, blank=False)
    size = models.CharField(max_length=30, choices=SIZE_CHOICES, default='Canvas size *')
    pet_num = models.CharField(max_length=30, choices=PET_NUM_CHOICES, default='Number of Pets *')
    media = models.CharField(max_length=40, choices=MEDIA_CHOICES, default= 'Media Preference *')
    message = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.email

