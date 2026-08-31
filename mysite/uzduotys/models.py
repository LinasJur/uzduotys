from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to = User, on_delete=models.CASCADE)

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

class TaskContent(models.Model):
    task = models.ForeignKey(to = Task, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to = User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
