from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm


def todo_list(request):
	incomplete_items = TodoItem.objects.filter(completed=False)
	# Completed_items are shown in the todoList_html
	completed_items = TodoItem.objects.filter(completed=True)
	return render(request, 'todolist/todo_list.html',
	              {'incomplete_items': incomplete_items, 'completed_items': completed_items})


# User mark the task complete.
def complete_todo_item(request, todo_id):
	todo_item = TodoItem.objects.get(id=todo_id)
	todo_item.completed = True
	todo_item.save()
	return redirect('todo_list')


def delete_todo_item(request, todo_id):
	if request.method == 'DELETE':
		TodoItem.objects.filter(id=todo_id).delete()
		return redirect('todo_list')


def update_todo_item(request, todo_id):
	record = TodoItem.objects.get(id=todo_id)
	if request.method == 'POST':
		form = TodoItemForm(request.POST, instance=record)
		if form.is_valid():
			form.save()
			return redirect('todo_list')
		else:
			form = TodoItemForm(instance=record)
		return render(request, 'todolist/update_todo_item.html', {'form':form})

	pass


def add_todo_item(request):
	if request.method == 'POST':
		form = TodoItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo_list')
	else:
		form = TodoItemForm()
	return render(request, 'todolist/add_todo_item.html', {'form': form})
