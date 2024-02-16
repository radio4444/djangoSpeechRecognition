from django.shortcuts import render, redirect
from .models import TodoList
from .form import TodoListForm


# Create your views here.

def testing(request):
	return render(request, 'todoList/testing.html')


def todolist(request):
	todo_items = TodoList.objects.filter(completed=False)
	return render(request, 'todoList/createTodo.html', {'todo_items': todo_items})


def complete_todo_items(request, todo_id):
	todo_item = TodoList.objects.filter(id=todo_id)
	todo_item.completed = False
	todo_item.save()
	return redirect('todo_list')


def add_todo_item(request):
	if request.method == 'POST':
		form = TodoListForm(request.POST)  # Create form using the data
		if form.is_valid():
			form.save()
			return redirect('todo_list')
		else:
			form = TodoListForm()  # Empty form
		return render(request, 'todoList/add_todo_item.html', {'form': form})
