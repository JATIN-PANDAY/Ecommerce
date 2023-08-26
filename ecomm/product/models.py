from django.db import models
from base.models import BaseModel
# Generate slug
from django.utils.text import slugify

# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    # category_image = models.ImageField(upload_to='categories',null=True)
    slug = models.SlugField (unique=True , null=True,blank=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
       return self.category_name



class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_image=models.ForeignKey('ProductImage', on_delete=models.CASCADE,null=True)

    def get_product_price_by_color(self,color):
        return self.price + ColorVariant.objects.get(color_name=color).price()
    
    



    def __str__(self):
        return self.color_name



class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=50)
    product = models.ForeignKey('Product', on_delete=models.CASCADE,null=True)
    # price = models.IntegerField(default=0)

    # def get_product_price_by_size(self,size):
    #     return self.price + SizeVariant.objects.get(size_name=size).price
    
    def __str__(self):
        return self.size_name



class Product(BaseModel):
    product_name = models.CharField(max_length=50)
    category =  models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50,null=True)
    price = models.IntegerField()
    product_description = models.TextField()
    image = models.ImageField(upload_to='product')

    slug = models.SlugField (unique=True , null=True,blank=True)
    # color_variant=models.ManyToManyField(ColorVariant,blank=True)
    # size_variant=models.ManyToManyField(SizeVariant,related_name='size',blank=True)    
   
    def save(self,*args,**kwargs):
        self.slug = slugify(self. product_name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.product_name

   
    def get_product_price_by_size(self,size):
        return self.price + SizeVariant.objects.get(size_name = size).price
    
    def get_product_price_by_color(self,color):
        return self.price + ColorVariant.objects.get(color_name=color).price




class ProductImage(BaseModel):
    product  = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product')
    # color_image=models.ForeignKey('ColorVariant',related_name='color', on_delete=models.CASCADE,null=True)

   