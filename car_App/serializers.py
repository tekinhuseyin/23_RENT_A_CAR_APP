from rest_framework import serializers
from .models import Car,Reservation

class CarSerializer(serializers.ModelSerializer):
    is_available=serializers.BooleanField()

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
                'is_available',
                )
        
    def get_fields(self):
        fields=super().get_fields()
        request=self.context.get('request')
        if request.user and not request.user.is_staff:
            fields.pop('plate_number')
            fields.pop('availability')
            fields.pop('rent_per_day')
        return fields




class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=(
                'customer',
                'car',
                'start_date',
                'end_date',
                )
    
 
  