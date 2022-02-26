from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/<slug:the_slug>', views.blogredirect, name='blog_redirect'),
    path('events/<slug:the_slug>', views.eventredirect, name='event_redirect'),
    path('register', views.register, name='register'),
    path('ccsresults', views.ccsresults, name='ccsresults'),
    path('registration', views.google_form, name='google_form'),
    path('join_our_group', views.group_invite, name='group_invite'),
]