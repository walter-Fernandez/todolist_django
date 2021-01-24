from django.contrib import admin

# Register your models here. --------> THAT'S RIGHT!!!
from .models import *
admin.site.register(Task)