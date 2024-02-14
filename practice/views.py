from django.shortcuts import render


# Create your views here.

def practice(request):
	return render(request, 'practice/helloWorld.html')


def input_form(request):
	if request.method == 'POST':
		user_input = request.POST.get('user_input', '')
		return render(request, 'practice/input_form.html', {'user_input': user_input})
	return render(request, 'practice/input_form.html')
