from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cliente
from .models import Mascota,MascotaCliente
from .models import User
from .forms import AgregarMascota, AgregarCliente
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.db.models import DEFERRED
import json
# Create your views here.

def inicio(request):
    return render (request,"inicio.html")

#*** USUARIOS ***#
def gestionCliente(request):  
    clientes=Cliente.objects.all()
    if request.method == 'POST':
        form = AgregarCliente(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            cli=User.objects.create_user(username=data.get("username"),email=data.get("email"),password=data.get("password"),first_name=data.get("first_name"),last_name=data.get("last_name"))
            cliente=Cliente(user=cli,telefono=data.get("telefono"),fec_nac=data.get("fec_nac"),region=data.get("region"),ciudad=data.get("ciudad"),tipo_vivienda=data.get("tipo_vivienda"))
            cliente.save()
            return redirect('inicio')   
    else:
        form = AgregarCliente()
    return render(request, 'gestionCliente.html', {'form':form,'clientes':clientes})

def verCliente(request,pk):
    cliente=Cliente.objects.get(codigoCliente=pk)
    return render(request,"verCliente.html",{'cliente':cliente})



def editarRescatado(request, pk):
    mascota=Mascota.objects.get(codigoMascota=pk)
    if request.method == "GET":
        form = AgregarMascota(instance=mascota)
    else:
        form = AgregarMascota(request.POST or None,request.FILES or None,instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('gestionMascota')
    return render(request, 'editarMascota.html', {'form':form})
    

def eliminarRescatado(request, pk):
    mascota=Mascota.objects.get(codigoMascota=pk)
    if request.method == "POST":
        mascota.delete()
        return redirect('gestionMascota')
    return render (request, 'eliminarMascota.html', {'mascota':mascota})


def listarMascotasDisponible(request):
    mascota=Mascota.objects.filter(estadoMascota="disponible")
    return render(request,"ListarMascotas.html")

#def listarMascotasDisponible(request):
 #   mascota=Mascota.objects.filter(estadoMascota="disponible")
  #  return render(request,"listarMascotasDisponibles.html",{'mascota':mascota})


def gestionMascota(request):
    form=AgregarMascota(request.POST or None,request.FILES or None)
    if form.is_valid():
        datos=form.cleaned_data
        regDb=Mascota(nombreMascota=datos.get("nombreMascota"),razaMascota=datos.get("razaMascota"),descripcionMascota=datos.get("descripcionMascota"),
        estadoMascota=datos.get("estadoMascota"),fotoMascota=datos.get("fotoMascota"))
        regDb.save()
    mascotas=Mascota.objects.all()
    contexto={
        'mascotas':mascotas,
        'form':form,
    }
    return render (request,"gestionMascota.html",contexto)


def solicitud(request,pk):
    clientes=Cliente.objects.all()
    mascotacliente=MascotaCliente.objects.all()
    User=request.user.username
    mascota=Mascota.objects.get(codigoMascota=pk)
    cliente=Cliente.objects.get(codigoCliente=pk)
    MascotaCliente.save(Cliente.user.username.get("username"),mascota.codigoMascota.get("codigoMascota"))
    return render(request,"solicitud.html",{'cliente':cliente,'mascota':mascota})


#LOGIN / LOGOUT
def ingresar(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request, user)
            return redirect('inicio')
    return render(request,"login.html",{'form':form})

def salir(request):
    logout(request)
    return redirect('inicio')

def base_layout(request):
  template='maqueta.html'
  return render(request,template)

def getdata(request):
  results=feed.objects.all()
  jsondata = serializers.serialize('json',results)
  return HttpResponse(jsondata)
