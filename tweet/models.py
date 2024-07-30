from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model) :
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='photos/tweet/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} {self.text[:20]}'