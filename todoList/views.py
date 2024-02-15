from django.shortcuts import render
from .models import TodoList
from .form import TodoListForm


# Create your views here.

def testing(request):
	return render(request, 'todoList/testing.html')


def todolist_form(request):
	if request.method == 'POST':
		form = TodoListForm(request.POST)  # Create form using the data
		if form.is_valid():
			form.save()
		else:
			form = TodoListForm()  # Empty form
		todolist = TodoList.objects.all()

		return render(request, 'todoList/createTodo.html',)
