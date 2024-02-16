from django.db import models


# Create your models here.
class TodoList(models.Model):
	PRIORITY_CHOICES = [
		('high', 'High'),
		('med', 'Medium'),
		('low', 'Low'),
	]
	task_name = models.CharField(max_length=200)
	dueDate = models.DateTimeField()
	completed = models.BooleanField(default=False)
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

	def __str__(self):
		return self.task_name
