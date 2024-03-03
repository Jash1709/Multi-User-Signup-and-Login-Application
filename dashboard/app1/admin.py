from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display=['usertype','firstname','lastname','email','username','password','line1','city','state','pincode','pphoto']

