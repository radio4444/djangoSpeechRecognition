from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm


def todo_list(request):
	incomplete_items = TodoItem.objects.filter(completed=False)
	completed_items = TodoItem.objects.filter(completed=True)
	return render(request, 'todolist/todo_list.html',
	              {'incomplete_items': incomplete_items, 'completed_items': completed_items})


def complete_todo_item(request, todo_id):
	todo_item = TodoItem.objects.get(id=todo_id)
	todo_item.completed = True
	todo_item.save()
	return redirect('todo_list')


def add_todo_item(request):
	if request.method == 'POST':
		form = TodoItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo_list')
	else:
		form = TodoItemForm()
	return render(request, 'todolist/add_todo_item.html', {'form': form})
