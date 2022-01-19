from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd

def home(request):
    result = ""
    if request.method == 'POST':
        reg = request.POST.get('registration')
        dataset = pd.read_csv("Result.csv", names=['Name', 'Registration'])
        dataset = pd.DataFrame(dataset)
        if reg in list(dataset['Registration']):
            result = "Pass"
        elif reg == "":
            result = "Invalid"
        else:
            result = "Fail"
    context = {"result" : result}
    return render(request, "index.html", context)