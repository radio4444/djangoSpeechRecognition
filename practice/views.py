from django.shortcuts import render
from .models import UserInfo
from .forms import UserForm


# Create your views here.
# a "view" refers to the Python function responsible for processing a web request and returning a web response.

def practice(request):
	return render(request, 'practice/helloWorld.html')


# Define a view function named user_info
def user_info(request):
	# Check if the request method is POST (i.e., form submission)
	if request.method == 'POST':
		# If it's a POST request, create a form instance with the submitted data
		form = UserForm(request.POST)
		# Check if the submitted form data is valid
		if form.is_valid():
			# If the form data is valid, save it to the database
			form.save()
	else:
		# If the request method is not POST (e.g., GET request), create an empty form
		# Example: Initial Page, Page refresh etc.
		form = UserForm()

	# Fetch all user information from the database
	users = UserInfo.objects.all()

	# Render the 'user_form.html' template with the form and user information
	return render(request, 'practice/user_form.html', {'form': form, 'users': users})
