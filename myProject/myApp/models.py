from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


class Product(models.Model):
    name = models.CharField(max_length=400)
    price = models.FloatField(max_length=10, default=0.0)
    image = models.ImageField(null=True, blank=True, upload_to="products/",default="products/product-default.png")
    description = RichTextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, max_length=400)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk, 'slug': self.slug})
    
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.name, self.create_at)

class Bicycle(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    