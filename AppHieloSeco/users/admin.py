from django.contrib import admin
from .models import Profile 

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user','type_user')

admin.site.register(Profile,ProfileAdmin)