from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy


# Create your models here.
class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """A custom manager to deal with emails and custom identifiers"""
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 
    def create_clients(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_clients = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must have is_staff=True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)

#Custom user model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_clients = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        gettext_lazy('staff_status'), default=False,
        help_text=gettext_lazy('designates whether the user can login to this site'),
    )

    is_active = models.BooleanField(
        gettext_lazy('active'), default=True,
        help_text=gettext_lazy('designates whether the user can loin to this site'),
    )

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

# Company Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    company_name = models.CharField(max_length=264, blank=True)
    company_type = models.CharField(max_length=50)
    lincense_no = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50) 
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    description = models.TextField( blank=True)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.company_name+"'s profile"

