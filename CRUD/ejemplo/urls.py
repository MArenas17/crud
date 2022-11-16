from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='index'),
    path('registrarcliente/', views.registrarcliente),
    path('actualizarcliente/<documento>',views.actualizarcliente ),
    path('eliminarCliente/<int:id>',views.eliminarCliente,name='eliminarCliente'),
    path('registrarCita/',views.registrarCita,name='registrarCita'),
    path('verCitas/',views.verCitas,name='verCitas'),
    path('actualizarCitas/<int:id>',views.actualizarCitas,name='actualizarCitas'),
    path('eliminarCita/<int:id>',views.eliminarCita,name='eliminarCita'),
]
