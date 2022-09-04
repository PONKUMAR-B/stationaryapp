from django.urls import include, path
from stationaryapp import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Product', views.ProductViewSet)

urlpatterns = [
   path('', include(router.urls)),
]