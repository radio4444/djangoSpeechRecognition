from django.urls import path
from . import views

urlpatterns = [
	path('', views.practice, name='practice-helloWorld'),
	path('input_form/', views.input_form, name='input_form'),
]
