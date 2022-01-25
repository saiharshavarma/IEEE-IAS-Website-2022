from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, request
from .models import Hyperlink, Blog, Event
import pandas as pd
import csv

registrations_file = "CCS Registrations.csv"

def home(request):
    result = None
    blog = Blog.objects.all()
    context = {"result" : result}
    context["blog1"] = blog[0]
    context["blog2"] = blog[1]
    context["blog3"] = blog[2]
    context["blog4"] = blog[3]
    context["blog5"] = blog[4]
    context["blog6"] = blog[5]
    return render(request, "index.html", context)

def blogredirect(request, the_slug):
    blog = Blog.objects.filter(slug = the_slug)[0]
    return redirect(blog.link) 

def register(request):
    result = None
    if request.method == 'POST':
        name = request.POST.get('name')
        regno = request.POST.get('regno')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print("in")
        dataset = pd.read_csv(registrations_file, names=['Name', 'Registration'])
        dataset = pd.DataFrame(dataset)
        if regno not in list(dataset['Registration']):
            with open(registrations_file, 'a', newline='') as csvfile:
                wrt = csv.writer(csvfile)
                wrt.writerow([name, regno, email, phone])
        else:
            return HttpResponse("User already present")
        context = {"result" : result}
        return HttpResponse("Successfully Registered " + name)
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

def success(request):
    return render(request, 'pass.html')

def fail(request):
    return render(request, 'fail.html')

def google_form(request):
    hyperlink = Hyperlink.objects.filter(id = 1)[0]
    return redirect(hyperlink.registration_google_form)

def group_invite(request):
    hyperlink = Hyperlink.objects.filter(id = 1)[0]
    return redirect(hyperlink.group_invite_link) 