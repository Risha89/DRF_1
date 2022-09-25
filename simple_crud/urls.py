from django.urls import path
from django.contrib import admin

from measurements.views import SensorsViewCreate, SensorViewUpdate, MeasurementCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorsViewCreate.as_view()),
    path('sensors/<pk>/', SensorViewUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    ]