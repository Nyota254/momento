from django.db import models

# Create your models here.
class Product (models.Model):
    """
    Article class defines Article objects
    """
    # CHOICES
    A2_SIZE = 'A2'
    A3_SIZE = 'A3'
    A4_SIZE = 'A4'
    A5_SIZE = 'A5'
    PRODUCT_SIZE_CHOICES = (
        (A2_SIZE, 'A2 Paper'),
        (A3_SIZE, 'A3 Paper'),
        (A4_SIZE, 'A4 Paper'),
        (A5_SIZE, 'A5 Paper'),
    )

    product_name = models.CharField(max_length=255, blank=False)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField (upload_to="static/product-image/", blank=True)
    product_size = models.CharField ('type',  max_length=3, choices=PRODUCT_SIZE_CHOICES)

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()

    def search_products(cls, search_term):
        products = cls.objects.filter(user__username__icontains=search_term)
        return products
