from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.viewsets import Cad_Taxista, Cad_Empresa

router = routers.DefaultRouter()
router.register(r'Ctaxista', Cad_Taxista, base_name='api_Ctaxi')
router.register(r'Cempresa', Cad_Empresa, base_name='api_Cempresa')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Taxi.urls')),
    path('api/', include(router.urls)),

]
