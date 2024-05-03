from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_images/")
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    weight = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=5)
    color = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return f"{self.name} at {self.price}"