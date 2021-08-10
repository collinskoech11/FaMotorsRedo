from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Contact(request):
    if request.method == 'POST':
        brand = request.POST.get('brand',"")
        email = request.POST.get('email',"")
        message = request.POST.get('message',"")

        contactForm = ContactForm(brand=brand, email=email, message=message)
        contactForm.save()

        
    return render(request, 'Contact.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, Your account was created successfully ')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form':form})

def Gallery(request):
    return render(request, 'Gallery.html')

def Recovery(request):
    return render(request, 'Recovery.html')

def Service(request):
    return render(request, 'Service.html')

def Team(request):
    return render(request, 'Team.html')

def Quotation(request):
    return render(request, 'quotation.html')

def Excess(request):
    return render(request, 'excess.html')

def Warranty(request):
    return render(request, 'warranty.html')