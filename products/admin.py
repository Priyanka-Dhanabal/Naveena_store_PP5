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
    list_display = (
        "product",
        "user",
        "rating",
        "comment",
        "created_at",
        "updated_at",
    )
    list_filter = ("product", "rating")
    search_fields = (
        "product__name",
        "user__username",
        "comment",
    )
    ordering = ("-created_at",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)