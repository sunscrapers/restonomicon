from django.contrib import admin
from .models import Friend, Belonging

admin.site.register([Friend, Belonging])