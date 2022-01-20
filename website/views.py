from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import csv

registrations_file = "CCS Registrations.csv"

def home(request):
    result = None
    context = {"result" : result}
    return render(request, "index.html", context)

def register(request):
    result = None
    if request.method == 'POST':
        name = request.POST.get('name')
        regno = request.POST.get('regno')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dataset = pd.read_csv(registrations_file, names=['Name', 'Registration'])
        dataset = pd.DataFrame(dataset)
        if regno not in list(dataset['Registration']):
            with open(registrations_file, 'a', newline='') as csvfile:
                wrt = csv.writer(csvfile)
                wrt.writerow([name, regno, email, phone])
        else:
            print("Already present")
        context = {"result" : result}
        return render(request, "index.html", context)
    else:
        return redirect('home')

def ccsresults(request):
    result = None
    if request.method == 'POST':
        reg = request.POST.get('registration')
        dataset = pd.read_csv(registrations_file, names=['Name', 'Registration'])
        dataset = pd.DataFrame(dataset)
        if reg in list(dataset['Registration']):
            result = "Pass"
        elif reg == "":
            result = "Invalid"
        else:
            result = "Fail"
        context = {"result" : result}
        return render(request, "index.html", context)
    else:
        return redirect('home')