from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, request
from .models import Hyperlink, Blog, Event
import pandas as pd
import csv

registrations_file = "CCS Registrations.csv"
context = {}

def home(request):
    result = None
    blog = Blog.objects.all()
    event = Event.objects.all()
    context["result"] = result
    context["blog1"] = blog[0]
    context["blog2"] = blog[1]
    context["blog3"] = blog[2]
    context["blog4"] = blog[3]
    context["blog5"] = blog[4]
    context["blog6"] = blog[5]
    context["event1"] = event[0]
    context["event2"] = event[1]
    context["event3"] = event[2]
    context["event4"] = event[3]
    return render(request, "index.html", context)

def blogredirect(request, the_slug):
    blog = Blog.objects.filter(slug = the_slug)[0]
    return redirect(blog.link) 

def eventredirect(request, the_slug):
    event = Event.objects.filter(slug = the_slug)[0]
    return redirect(event.link) 

def register(request):
    result = None
    blog = Blog.objects.all()
    event = Event.objects.all()
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
        context["result"] = result
        context["blog1"] = blog[0]
        context["blog2"] = blog[1]
        context["blog3"] = blog[2]
        context["blog4"] = blog[3]
        context["blog5"] = blog[4]
        context["blog6"] = blog[5]
        context["event1"] = event[0]
        context["event2"] = event[1]
        context["event3"] = event[2]
        context["event4"] = event[3]
        return HttpResponse("Successfully Registered " + name)
    else:
        return redirect('home')

def ccsresults(request):
    result = None
    blog = Blog.objects.all()
    event = Event.objects.all()
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
        context["result"] = result
        context["blog1"] = blog[0]
        context["blog2"] = blog[1]
        context["blog3"] = blog[2]
        context["blog4"] = blog[3]
        context["blog5"] = blog[4]
        context["blog6"] = blog[5]
        context["event1"] = event[0]
        context["event2"] = event[1]
        context["event3"] = event[2]
        context["event4"] = event[3]
        return render(request, "index.html", context)
    else:
        return redirect('home')

def success(request):
    return render(request, 'pass.html')

def fail(request):
    return render(request, 'fail.html')

def google_form(request):    
    hyper = Hyperlink.objects.filter(id = 1)[0]
    return redirect(hyper.registration_google_form)

def group_invite(request):
    hyper = Hyperlink.objects.filter(id = 1)[0]
    return redirect(hyper.group_invite_link) 