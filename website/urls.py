from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('ccsresults', views.ccsresults, name='ccsresults'),
    path('registration', views.google_form, name='google_form'),
    path('join_our_group', views.group_invite, name='group_invite'),
    path('pass', views.success, name='pass'),
    path('fail', views.fail, name='fail'),
]