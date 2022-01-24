from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('ccsresults', views.ccsresults, name='ccsresults'),
    path('pass', views.success, name='pass'),
    path('fail', views.fail, name='fail'),
]