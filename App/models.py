from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICE = (
    ('ACTIVE', 'ACTIVE'),
    ('INACTIVE', 'INACTIVE'),
)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    strap_color = models.CharField(max_length=100)
    highlight = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length = 20,choices = STATUS_CHOICE)
    
    
    
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    