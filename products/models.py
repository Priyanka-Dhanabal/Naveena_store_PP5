from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def update_rating(self):
        """Calculate and update the average rating based on
        associated reviews."""
        reviews = self.reviews.all()
        if reviews.exists():
            self.rating = round(
                sum(review.rating for review in reviews) / reviews.count(), 2
            )
        else:
            self.rating = None
        self.save()

    def get_absolute_url(self):
        """Return the URL to the product detail page."""
        return reverse("product_detail", args=[str(self.id)])

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [
            "product",
            "user",
        ]  # Ensure one review per user per product

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name} ({self.rating}/5)"
