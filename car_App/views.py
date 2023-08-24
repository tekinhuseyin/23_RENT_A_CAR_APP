from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer,ReservationSerializer
from .models import Car,Reservation
# Create your views here.

class CarView(ModelViewSet):
    serializer_class=CarSerializer
    queryset=Car.objects.all()


class ReservationView(ModelViewSet):
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()