from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200) 

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name=models.CharField(max_length=200) 
    condition=models.CharField(max_length=200)
    price=models.PositiveIntegerField() 
    picture=models.ImageField(upload_to="product_pic",null=True, blank=True)
    place=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    status_option={
        ("sold","sold"),
        ("available","available")

    }
    status=models.CharField(max_length=200,choices=status_option,default="available")


    def __str__(self):
        return self.name


