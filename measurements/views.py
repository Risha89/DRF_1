from rest_framework import generics

from measurements.models import Sensor, Measurement
from measurements.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorsViewCreate(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer