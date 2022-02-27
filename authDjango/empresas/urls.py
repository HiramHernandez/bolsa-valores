from django.urls import path, include
from .views import EmpresaListController, CheckAuth

urlpatterns = [
    path('empresas/', EmpresaListController.as_view(), name='empresa-list'),
     path('hola/', CheckAuth.as_view(), name='check-auth')
]
