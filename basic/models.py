from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70, db_index=True)
    slug = models.SlugField(max_length=70, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.title
