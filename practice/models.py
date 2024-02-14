from django.db import models


# Create your models here.
class UserInfo(models.Model):
	name = models.TextField()
	email = models.EmailField()
	address = models.TextField()
	phoneNumber = models.IntegerField()
