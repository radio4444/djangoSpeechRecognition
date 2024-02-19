from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo_list, name='todo_list'),
	path('complete/<int:todo_id>/', views.complete_todo_item, name='complete_todo_item'),
	path('delete/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
	path('add/', views.add_todo_item, name='add_todo_item'),
	path('update/<int:todo_id>/', views.update_todo_item, name='update_todo_item'),
]
