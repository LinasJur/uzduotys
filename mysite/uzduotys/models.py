from django.contrib.auth.models import User, AbstractUser
from django.db import models

import uzduotys


class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to ='uzduotys.CustomUser', on_delete=models.CASCADE)

    ORDER_STATUS = (
        ('s' , 'Sukurta'),
        ('v' , 'Vykdoma'),
        ('a' , 'Atšaukta'),
        ('į' , 'Įvykdyta'),
    )
    status = models.CharField(verbose_name="Status", max_length=1, choices=ORDER_STATUS, blank=True, default='s')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='profile_pics', blank=True, null=True)

