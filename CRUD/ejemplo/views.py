from django.shortcuts import render,redirect
from . models import cliente
from .forms import *

# Create your views here.
def home (request):
    clientes=cliente.objects.all()
    return render (request, "iniciar.html", {"clientes":clientes})

def registrarcliente(request):
    client = cliente()
    client.documento = request.POST.get('documento')
    client.nombre = request.POST.get ('nombre')
    client.apellido = request.POST.get ('apellido')
    client.edad = request.POST.get ('edad')
    client.email = request.POST.get ('email')
    client.ciudad = request.POST.get ('ciudad')
    client.genero = request.POST.get ('genero')
    client.telefono = request.POST.get ('telefono')
    client.fechanacimiento = request.POST.get ('fechanacimiento')
    client.estadocivil = request.POST.get ('estadocivil')
    client.save()
    return redirect('index')

def actualizarcliente(request,documento):
    clientes = cliente.objects.get(documento = documento)
    return render (request, "actualizar.html", {"clientes",cliente})

def eliminarCliente(request,id):
    clientes = cliente.objects.get(id = id)
    clientes.delete()
    return redirect('index')

def registrarCita(request):
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('verCitas')
    else:
        form = CitasForm()
    return render(request,'registrarCita.html',{'form': form})

def actualizarCitas(request,id):
    cita = Citas.objects.get(id = id)
    if request.method == 'POST':
        form = CitasForm(request.POST, instance= cita)
        if form.is_valid:
            form.save()
            return redirect('verCitas')
    else: 
        form = CitasForm(instance = cita)
    return render(request,'registrarCita.html',{'form':form})


def verCitas(request):
    citas = Citas.objects.all()
    return render(request,'verCitas.html',{'citas':citas})

def eliminarCita(request,id):
    citas = Citas.objects.get(id=id)
    citas.delete()
    return redirect('verCitas')



