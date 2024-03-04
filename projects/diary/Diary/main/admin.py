from django.contrib import admin
from .models import Diary,Color #import class so it also show it

admin.site.register(Diary)
admin.site.register(Color)
