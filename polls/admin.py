from django.contrib import admin

# Register your models here.
from .models import Poll
from .models import Poll_Trigger

admin.site.register(Poll)
admin.site.register(Poll_Trigger)
