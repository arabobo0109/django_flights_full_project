from django.contrib import admin
from .models import Flight, User, SoundList, Sound

# Register your models here.
admin.site.register(Flight)
admin.site.register(User)
admin.site.register(SoundList)
admin.site.register(Sound)