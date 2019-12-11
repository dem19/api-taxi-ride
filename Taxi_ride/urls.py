from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.viewsets import ListagemTaxista

router = routers.DefaultRouter()
router.register(r'listagem', ListagemTaxista, base_name='api_Ltaxi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Taxi.urls')),
    path('api/', include(router.urls)),

]
