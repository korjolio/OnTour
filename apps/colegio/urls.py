from django.urls import path, re_path
from .views import Home, crearContrato, listarContrato, editarContrato, eliminarContrato

urlpatterns = [
    path('', Home, name = 'home'),
    path('crear_contrato/', crearContrato, name = 'crear_contrato'),
    path('listar_contrato/', listarContrato, name = 'listar_contrato'),
    path('editar_contrato/<int:id_contrato>', editarContrato, name = 'editar_contrato'),
    path('eliminar_contrato/<int:id_contrato>', eliminarContrato, name = 'eliminar_contrato'),

    
]