from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarcliente/', views.registrarcliente),
    path('actualizarcliente/<documento>',views.actualizarcliente ),
    path('eliminarcliente/<documento>',views.eliminarcliente),
]
