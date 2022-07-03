from django.contrib import admin
from .models import Sensors, Monitoring

# Register your models here.
admin.site.register(Sensors)
admin.site.register(Monitoring)
