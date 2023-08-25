from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import CarSerializer,ReservationSerializer
from .models import Car,Reservation
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import IsAdminOrReadOnly
from django.db.models import Q,OuterRef,Exists
from django.utils import timezone
from rest_framework.response import Response
# Create your views here.

class CarView(ModelViewSet):
    serializer_class=CarSerializer
    queryset=Car.objects.all()
    permission_classes=[IsAdminOrReadOnly,]

    def get_queryset(self):
        
        if self.request.user.is_staff:
            queryset=super().get_queryset().filter()
        else:
            queryset=super().get_queryset().filter(availability=True)
      

        start=self.request.query_params.get('start')
        end=self.request.query_params.get('end')
        # if start is not None and end is not None:   
        if start and end:      
            #select id from reservation where end_date>start and start_date<end

            # not_available=Reservation.objects.filter(
            #     end_date__gt=start,start_date__lt=end
            #     ).values_list('id',flat=True) 

            #flat true id leri [1,3,7] listeye çeviriyor
            # queryset=self.queryset.exclude(id__in=not_available)

            # not_available=Reservation.objects.filter(
            #     Q(end_date__gt=start) & Q(start_date__lt=end)
            #     ).values_list('id',flat=True) 
            c1=Q(end_date__gt=start)
            c2=Q(start_date__lt=end)
            # not_available=Reservation.objects.filter(
            #     c1 & c2
            #     ).values_list('id',flat=True) 

            # queryset=queryset.exclude(id__in=not_available)
            
            #SQL join
            queryset=queryset.annotate(
                is_available= ~Exists(Reservation.objects.filter(
                    Q(car=OuterRef('pk')) & c1 & c2
                    )
                )
            )


        return queryset
    

class ReservationView(ListCreateAPIView):
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(customer=self.request.user)
    
class ReservationRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()
    permission_classes=[IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        today=timezone.now().date()
        car=instance.car
        # start=instance.start_date
        # end=instance.end_date
        end=serializer.validated_data.get("end_date")
        start=serializer.validated_data.get("start_date")

        print ("*********instance")
        print(car)
        print(start)
        print(end)

        car_reservations=Reservation.objects.filter(car=car,end_date__gte=today)
        if car_reservations:
            for res in car_reservations:
                if (res.start_date  <start < res.end_date) or (res.start_date  < end < res.end_date):
                    return Response({'message':'you can not update reservation for this dates'})
        
        return super().update(request, *args, **kwargs)        


