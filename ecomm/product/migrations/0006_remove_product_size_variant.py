# Generated by Django 4.2.4 on 2023-08-14 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_size_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size_variant',
        ),
    ]
