from django.shortcuts import render, redirect, get_object_or_404
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
	TodoItem.objects.filter(id=todo_id).delete()
	return redirect('todo_list')


def update_todo_item(request, todo_id):
	todo_item = get_object_or_404(TodoItem, id=todo_id)
	if request.method == 'POST':
		form = TodoItemForm(request.POST, instance=todo_item)
		if form.is_valid():
			form.save()
			return redirect('todo_list')
	else:
		form = TodoItemForm(instance=todo_item)
	return render(request, 'todolist/update_todo_item.html', {'form': form})


def add_todo_item(request):
	if request.method == 'POST':
		form = TodoItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo_list')
	else:
		form = TodoItemForm()
	return render(request, 'todolist/add_todo_item.html', {'form': form})


def sort_todo_item(request):  # chatgpt
	if request.method == 'POST':
		sort_property = request.POST.get('sort_property')
		sort_order = request.POST.get('sort_order')

		# Fetch incomplete and complete todo items separately
		incomplete_items = TodoItem.objects.filter(completed=False)
		completed_items = TodoItem.objects.filter(completed=True)

		# Sort incomplete and complete todo items based on the selected property and order
		if sort_order == 'asc':
			incomplete_items = incomplete_items.order_by(sort_property)
			completed_items = completed_items.order_by(sort_property)
		else:
			incomplete_items = incomplete_items.order_by(f'-{sort_property}')
			completed_items = completed_items.order_by(f'-{sort_property}')

		return render(request, 'todolist/todo_list.html',
		              {'incomplete_items': incomplete_items, 'completed_items': completed_items})
	else:
		# Handle GET request if needed
		pass
