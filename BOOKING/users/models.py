from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(null=True, blank=True)
    objects = UserManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']



    def __str__(self):
        return self.email


class HostProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='host')
    name = models.CharField(max_length=100)
    bio = models.TextField()
    is_verified = models.BooleanField(default=False)
    host_since = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}:{self.host_since}"






