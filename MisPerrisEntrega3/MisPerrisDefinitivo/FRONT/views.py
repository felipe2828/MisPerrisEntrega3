from django.shortcuts import render

# Create your views here.
def ListaMascotas(request):
    return render(request,"ListarMascotas.html")
