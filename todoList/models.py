from django.db import models


# Create your models here.
class TodoList(models.Model):
	todoListName = models.CharField(max_length=100)
	dueDate = models.DateTimeField()
	checkBox = models.BooleanField()
	priority = models.TextChoices('High', 'Med', 'Low')
