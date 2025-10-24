from django.shortcuts import render,redirect
from .forms import StallRegistrationForm

# Create your views here.

def index(request):
    # This tells Django to find 'index.html' in your 'templates'
    # folder, process it, and return it as a response.
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = StallRegistrationForm(request.POST) # <-- Change this
        if form.is_valid():
            form.save() 
            return redirect('register_success')
    else:
        form = StallRegistrationForm() # <-- Change this

    return render(request, 'main/register.html', {'form': form})

def register_success(request):
    return render(request, 'main/register_success.html')