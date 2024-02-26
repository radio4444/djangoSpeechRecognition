from django.db import models


class TodoItem(models.Model):
	PRIORITY_CHOICES = [
		('high', 'High'),
		('med', 'Medium'),
		('low', 'Low'),
	]
	task_name = models.CharField(max_length=200)
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
	due_date = models.DateField()
	completed = models.BooleanField(default=False)
	description = models.TextField(max_length=300, null=True, blank=True)

	def __str__(self):
		return self.task_name
