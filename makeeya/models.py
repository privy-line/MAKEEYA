from django.db import models
from tinymce.models import HTMLField
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
=======
from .email import send_notification_email
>>>>>>> origin

class Buyer(models.Model):
    first_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length =100)
    email = models.EmailField()

<<<<<<< HEAD
class Request(models.Model):
  business_name = models.CharField(max_length =100)
  business_identification_number = models.CharField(max_length =100)
  prefered_username = models.CharField(max_length =100)
  business_phone_number = models.IntegerField ()
  business_email = models.EmailField()
  Business_address = models.CharField(max_length =100) 

  def __str__(self):
        return self.name

  def save_request(self):
        self.save()
    
=======
class Profile(models.Model):
  business_name = models.CharField(max_length =100)
  business_description = HTMLField()
  business_logo = models.ImageField(upload_to='Buyer/',blank=True)
  business_email = models.EmailField() 
  business_address = models.CharField(max_length =100)


>>>>>>> origin

class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
  business_name = models.CharField(max_length =100)
  business_description = HTMLField()
  business_logo = models.ImageField(upload_to='Buyer/',blank=True)
  business_email = models.EmailField() 
  business_address = models.CharField(max_length =100)
  request = models.OneToOneField(Request,on_delete=models.CASCADE,blank=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Category(models.Model):
  name = models.CharField(max_length =100)

class Item(models.Model):
  name = models.CharField(max_length =100)
  picture = models.ImageField(upload_to='Buyer/',blank=True)
  original_Price = models.IntegerField()
  current_price = models.IntegerField() 
  expiry_date = models.DateTimeField(auto_now_add=False)
  category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=False) 
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=False) 


   
<<<<<<< HEAD
=======
class Request(models.Model):
  business_name = models.CharField(max_length =100)
  business_identification_number = models.CharField(max_length =100)
  prefered_username = models.CharField(max_length =100)
  business_phone_number = models.IntegerField ()
  business_email = models.EmailField()
  Business_address = models.CharField(max_length =100) 

  def __str__(self):
        return self.name

  def save_request(self):
        self.save()
    
    
>>>>>>> origin
   
 

 

  
    
