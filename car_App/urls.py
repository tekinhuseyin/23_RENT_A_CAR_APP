from django.urls import path,include
# from .views import RegisterView
from rest_framework.routers import DefaultRouter
from .views import CarView,ReservationView,ReservationRUDView

router=DefaultRouter()
router.register('car',CarView)

urlpatterns = [
    # path('auth/', include('dj_rest_auth.urls')),
    path('reservation/',ReservationView.as_view()),
    path('reservation/<int:pk>/',ReservationRUDView.as_view()),
    # path('', include(router.urls)),

]
urlpatterns+=router.urls