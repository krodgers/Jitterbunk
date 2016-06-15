from django.contrib import admin

from .models import Bunk, UserProfile

# Register your models here.




admin.site.register(UserProfile)
admin.site.register(Bunk)

