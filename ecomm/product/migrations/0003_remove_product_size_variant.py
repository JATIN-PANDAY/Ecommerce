# Generated by Django 4.2.4 on 2023-08-14 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_productimage_color_image_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size_variant',
        ),
    ]