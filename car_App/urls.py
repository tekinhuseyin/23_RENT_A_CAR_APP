from django.urls import path,include
# from .views import RegisterView
from rest_framework.routers import DefaultRouter
from .views import CarView,ReservationView

router=DefaultRouter()
router.register('car',CarView)

urlpatterns = [
    # path('auth/', include('dj_rest_auth.urls')),
    # path('register/',RegisterView.as_view()),
    # path('', include(router.urls)),
]
urlpatterns+=router.urls