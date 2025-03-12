from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    search_fields = ("name", "sku")  # Enable search by name and SKU
    ordering = ("sku",)
    readonly_fields = (
        "rating",
    )  # Make rating visible but read-only in the detail view


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """Admin interface for managing Review objects."""

    list_display = (
        "product",
        "user",
        "rating",
        "comment",
        "created_at",
        "updated_at",
    )
    list_filter = ("product", "rating")  # Filter by product and rating
    search_fields = (
        "product__name",
        "user__username",
        "comment",
    )  # Search by product name, username, and comment
    ordering = ("-created_at",)  # Order by the newest reviews first

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)