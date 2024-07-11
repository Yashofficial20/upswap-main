from django.contrib import admin
from .models import Signup
# Register your models here.

class SignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'phone_number')

admin.site.register(Signup, SignupAdmin)