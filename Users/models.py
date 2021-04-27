from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.

class Users_Manager(BaseUserManager):
    def create_user(self,email,phone,name,password=None):
        # if not email:
        #     raise ValueError ("Email is required")

        # if not phone:
        #     raise ValueError ("Phone Number is required")

        # if not name:
        #     raise ValueError ("Name  is required")
        
        user = self.model(email = self.normalize_email(email),
                          phone = phone,
                          name = name )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,phone,name,password=None):
        user = self.create_user(email = self.normalize_email(email),
                          phone = phone,
                          name = name,
                          password=password )
        user.save(using = self._db)

        
    
class User(AbstractBaseUser):
    name                       = models.CharField(max_length=50,null=False,blank=False)
    email                      = models.EmailField(max_length = 50,null=False,blank=False,unique=True)
    phone                      = models.CharField(max_length=10,null=False,blank=False)
    password                   = models.CharField(max_length=1024,null=False,blank=False)
    registered_on              = models.DateTimeField(auto_now_add=True)

    #additional fields non-login authentication fields
    customer_id                = models.CharField(max_length=25,null=True,blank=True)
    is_admin                   = models.BooleanField(default=False)
    is_staff                   = models.BooleanField(default=False)
    is_superadmin              = models.BooleanField(default=False)
    address1                   = models.TextField(null=True,blank=True)
    address2                   = models.TextField(null=True,blank=True)
    other_address              = models.TextField(null=True,blank=True)
    payment_details            = models.TextField(null=True,blank=True)
    total_orders_placed        = models.PositiveIntegerField(null=True,blank=True)
    total_orders_canceled      = models.PositiveIntegerField(null=True,blank=True)
    total_orders_sucessful     = models.PositiveIntegerField(null=True,blank=True)
    total_times_dispute_raised = models.PositiveIntegerField(null=True,blank=True)
    phone_number_verfied       = models.BooleanField(default=False)
    mail_verified              = models.BooleanField(default=False)
    is_active                  = models.BooleanField(default=True)




    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","phone"]

    objects = Users_Manager()

    def __str__(self):
        return self.email 



