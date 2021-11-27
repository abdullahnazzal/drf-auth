from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Profile(AbstractUser):
    email = models.EmailField(unique=True , max_length=255,verbose_name = "Email Address")
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(choices=(('Male','male'), ('Female','female')), max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'gender', 'username']
    
    def __str__(self):
        return self.email