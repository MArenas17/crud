from django.shortcuts import render,redirect
from . models import cliente 

# Create your views here.
def home (request):
    clientes=cliente.objects.all()
    return render (request, "iniciar.html", {"clientes":clientes})

def registrarcliente(request):
    documento = request.POST.get['documento']
    nombre = request.POST.get ['nombre']
    apellido = request.POST.get ['apellido']
    edad = request.POST.get ['edad']
    email = request.POST.get ['email']
    ciudad = request.POST.get ['ciudad']
    genero = request.POST.get ['genero']
    telefono = request.POST.get ['telefono']
    fechanacimiento = request.POST.get ['fechanacimiento']
    estadocivil = request.POST.get ['estadocivil']

    clientes = cliente.objects.create( documento = documento,nombre = nombre, apellido = apellido, edad = edad, email = email, ciudad = ciudad,  genero = genero, telefono = telefono, fechanacimiento = fechanacimiento,  estadocivil =  estadocivil )
    return redirect('/registarcliente/')

def actualizarcliente(request,documento):
    clientes = cliente.objects.get(documento = documento)
    return render (request, "actualizar.html", {"clientes",cliente})

def eliminarcliente(request,documento):
    clientes = cliente.objects.get(documento = documento)
    cliente.delete()
    return redirect('/eliminarcliente/')



