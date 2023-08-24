from rest_framework import serializers
from .models import Car,Reservation

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=(
                'plate_number',
                'brand',
                'model',
                'year',
                'gear',
                'rent_per_day',
                'availability',
                )


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=(
                'customer',
                'car',
                'start_date',
                'end_date',
                )
    
 
  