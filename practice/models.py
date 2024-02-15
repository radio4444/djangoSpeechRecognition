from django.db import models


# Create your models here.
# a model is a Python class that represents a table in the database
class UserInfo(models.Model):
	name = models.TextField()
	email = models.EmailField()
	address = models.TextField()
	phone_number = models.IntegerField()
