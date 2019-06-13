from django.db import models
from tinymce.models import HTMLField

class Buyer(models.Model):
    first_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length =100)
    email = models.EmailField()

class Seller(models.Model):
  business_name = models.CharField(max_length =100)
  business_description = HTMLField()
  business_logo = models.ImageField(upload_to='Buyer/',blank=True)
  business_email = models.EmailField() 
  business_address = models.CharField(max_length =100)



class Category(models.Model):
  name = models.CharField(max_length =100)

class Item(models.Model):
  name = models.CharField(max_length =100)
  picture = models.ImageField(upload_to='Buyer/',blank=True)
  original_Price = models.IntegerField()
  current_price = models.IntegerField() 
  expiry_date = models.DateTimeField(auto_now_add=False)
  category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=False) 
  seller = models.ForeignKey(Seller,on_delete=models.CASCADE,blank=False) 


   
class Request(models.Model):
  name = models.CharField(max_length =100)
  Identification_number = models.CharField(max_length =100)
  prefered_username = models.CharField(max_length =100)
  phone_number = models.IntegerField ()
  email = models.EmailField() 

  def __str__(self):
        return self.name

  def save_request(self):
        self.save()
    
    
   
 

 

  
    
