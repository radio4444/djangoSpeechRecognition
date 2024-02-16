from django.urls import path
from . import views

urlpatterns = [
	path('', views.testing, name='testing'),
	path('add/', views.add_todo_item, name='add_todo_item'),
	path('complete/<int:todo_id>/', views.complete_todo_items, name='complete_todo_item'),
]
