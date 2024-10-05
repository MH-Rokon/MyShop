from django.db import models
import datetime

# Model for  store product Category
class Category(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/category/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta :
       verbose_name_plural = 'Categories'

# Model for  store Customer Information
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} '
    

# Model for store Product of the store
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.TextField(max_length=500,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads/product/')
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    
    def __str__(self):
        return self.name
    

# Model for store the order inoformation 
class Order(models.Model):
    product=models.ForeignKey('Product', on_delete=models.CASCADE)
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE)
    quality=models.IntegerField(default=1)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=20)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.product
 
 
