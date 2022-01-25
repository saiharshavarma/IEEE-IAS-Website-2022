from django.contrib import admin
from .models import Hyperlink, Blog, Event

# Register your models here.
admin.site.register(Hyperlink)
admin.site.register(Blog)
admin.site.register(Event)