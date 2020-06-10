from django.db import models
from django.db.models import Sum, Avg
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from pytils import translit


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
    lower_city_name = models.TextField(default='')
    lower_name = models.TextField(default='')

    def get_image_mainpage(self):
        return Attachment.objects.all().filter(id_Attraction_id=self.id)[0].photo

    def count_avg_mark(self):
        res = Mark.objects.all().filter(id_Attraction_id=self.id).aggregate(Avg('value'))
        val = res.get('value__avg')
        if val is None:
            return 'Нет оценок'
        else:
            return round(val, 2)


class Attachment(models.Model):

    def get_image_path(self, filename):
        path = ''.join(["attachments/", translit.slugify(filename)])
        return path

    photo = models.FileField(upload_to=get_image_path)
    id_Attraction = models.ForeignKey(Attractions, default='', on_delete=models.CASCADE)


class Mark(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField(default='')
    id_Attraction = models.ForeignKey(Attractions, default='', on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
