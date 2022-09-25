from django.contrib import admin

from measurements.models import Sensor, Measurement

admin.site.register(Sensor)
admin.site.register(Measurement)
