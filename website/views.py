from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from json import dumps
from .models import Hyperlink, Blog, Event
import pandas as pd
import csv
import re

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
    f_name = None
    f_reg = None
    blog = Blog.objects.all()
    event = Event.objects.all()
    if request.method == 'POST':
        reg = (request.POST.get('registration')).upper()
        dataset = open("CCS Registrations.csv", "r")
        reader = csv.DictReader(dataset)
        if not re.match(r"^2[0,1][A-Za-z]{3}[0-9]{4}$", reg):
            result = "Invalid"
        else:
            for row in reader:
                if reg in row['Registration']:
                    result = "Pass"
                    f_name = row['Name']
                    f_reg = row['Registration']
                    break
                else:
                    result = "Fail"
        
        student_details = {'result': result,
            'name': f_name,
            'reg': f_reg
        }
        student_details = dumps(student_details)
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
        return HttpResponse(student_details)
        #return render(request, "index.html", context)
    else:
        return redirect('home')

def google_form(request):    
    hyper = Hyperlink.objects.filter(id = 1)[0]
    return redirect(hyper.registration_google_form)

def group_invite(request):
    hyper = Hyperlink.objects.filter(id = 1)[0]
    return redirect(hyper.group_invite_link) 