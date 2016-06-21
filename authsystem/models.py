from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):

    id = models.IntegerField(primary_key=True)
    displayName = models.CharField(max_length=20, null=False, default="None")
    user = models.ForeignKey(User)
    gender = models.CharField(max_length=10)
    avatar = models.ImageField(null=True,default='user.png', upload_to='static/')

    def __str__(self):

        return self.user.username