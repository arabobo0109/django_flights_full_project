from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
# from .models import Flight, User, SoundList, Sound
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

admin.site.register(MyUser)



# Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class CustomerInline(admin.StackedInline):
#     model = Customer
#     can_delete = False
#     verbose_name_plural = "employee"


# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = [CustomerInline]


# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

