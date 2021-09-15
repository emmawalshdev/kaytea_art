from django.db import models
from django.core.validators import MaxValueValidator

from django.contrib.auth.models import User  


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True, null=True) 
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length="100", null=True, blank=True)
    size = models.CharField(max_length=100)
    media = models.CharField(max_length=100)
    stock = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


RATING = (
    ('', 'Rating *'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class ProductReview(models.Model):
    author = models.ForeignKey(User, null=True,
                               blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.CharField(choices=RATING,
                                     max_length=1,
                                     default='Rating *')

    def __str__(self):
        return f'{self.product} review by {self.author}'
