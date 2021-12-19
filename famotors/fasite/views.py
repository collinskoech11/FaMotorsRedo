from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ContactForm
"""Self Describing Numbers
Programming challenge description:
A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number.
Input:
Your program should read lines of text from standard input. Each line contains a single positive integer, N.
Output:
For each input N, print 1 to standard output if N is a self-describing number. Otherwise, print 0.

For the curious, here''s how 2020 is a self-describing number: Position 0 has value 2 and there are two 0s in the number. Position 1 has value 0 because there are no 1's in the number. Position 2 has value 2 and there are two 2's. And the position 3 has value 0 and there are zero 3's.
Test 1

import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

for line in sys.stdin:
    if "1" in line:
        stri = reuonnoinfe
    if "2" in line:
        stri = oesowufxrzohgiettr
    if "3" in line:
        stri = "veiifogvweesotwnetnvfeheiot"
    if "4" in line:
        stri = "xtneiootnrnoeneeeeuoeoheetehounzoiuetrhfefeezuivirfwieotgoottfnrnneghetserhrwsgesfherhtiitrerevreernhveo"
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    array = [0] * (10)
    ans = ""
    n = len(stri)
    for i in range(n):
        if (stri[i] == 'z'):
            array[0] += 1
        if (stri[i] == 'w'):
            array[2] += 1
        if (stri[i] == 'g'):
            array[8] += 1
        if (stri[i] == 'x'):
            array[6] += 1
        if (stri[i] == 'v'):
            array[5] += 1
        if (stri[i] == 'o'):
            array[1] += 1
        if (stri[i] == 's'):
            array[7] += 1
        if (stri[i] == 'f'):
            array[4] += 1
        if (stri[i] == 'h'):
            array[3] += 1
        if (stri[i] == 'i'):
            array[9] += 1
            
            
    array[7] += array[6]
    array[5] += array[7]
    array[4] += array[5]
    array[1] += (array[2] + array[4] + array[0])
    array[3] += array[8]
    array[9] += (array[5] + array[6] + array[8])
    
    
    for i in range(10):
        for j in range(array[i]):
            ans += chr((i) + ord('0'))
            
    print(ans)


"""
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