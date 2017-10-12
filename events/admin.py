from django.contrib import admin
from .models import Branch, Event, Participants

# Register your models here.

admin.site.register(Branch)
admin.site.register(Event)
admin.site.register(Participants)