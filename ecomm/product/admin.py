from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Category)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


# class SizeVariantAdmin(admin.StackedInline):
#     model = Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price']
    inlines = [ProductImageAdmin]

# Register Color and Size Variant

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name','price']
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name','product']
    model = SizeVariant



admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
# admin.site.register(SizeVariant)

