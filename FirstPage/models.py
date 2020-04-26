from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField('email address', unique=True)
    nickname = models.CharField('nickname', max_length=30, blank=True)
    is_moderator = models.BooleanField(default=False)
    is_staff = models.BooleanField('staff status', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Attractions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='')
    descriptions = models.TextField(default='')
    city_name = models.TextField(default='')
    type = models.TextField(default='')
    address = models.TextField(default='', null=True)
    is_approved = models.BooleanField(default=False)
    photo = models.ImageField(default='', upload_to='')


class Mark(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField(default='')
    id_Attraction = models.ForeignKey(Attractions, default='', on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
