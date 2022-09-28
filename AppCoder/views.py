from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *

# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def relojes(request):

    reloj1 = Relojes(nombre="Samsung", modelo=250)
    reloj1.save()

    return render(request, "AppCoder/relojes.html")

def Billeteras(request):

    return render(request, "AppCoder/billeteras.html")

def Lentes(request):

    return render(request, "AppCoder/lentes.html")


    ################################################################################  

def relojesFormulario(request):

    if request.method == "POST":

        formulario1 = RelojesFormulario(request.POST)

        if formulario1.is_valid():
         
            info = formulario1.cleaned_data

            reloj = Relojes(nombre=info["reloj"], modelo=info["modelo"])

            reloj.save()

            return render(request, "AppCoder/inicio.html")

    else: 
        formulario1 = RelojesFormulario()

    return render(request, "AppCoder/relojesFormulario.html", {"form1":formulario1} )

    ################################################################################

def billeterasFormulario(request):

    if request.method == "POST":

        formulario2 = BilleterasFormulario(request.POST)

        if formulario2.is_valid():

            info= formulario2.cleaned_data

            billetera = billeteras(nombreBilletera=info["nombreBilleteras"])    #model , luego forms

            billetera.save()

            return render(request, "AppCoder/inicio.html")

    else: 
        formulario2 = BilleterasFormulario()

    return render(request, "AppCoder/BilleterasFormulario.html", {"form2":formulario2} )

 

def lentesFormulario(request):

    if request.method == "POST":

        formulario3 = LentesFormulario(request.POST)

        if formulario3.is_valid():

            info= formulario3.cleaned_data

            lentes1 = lentes(nombreLentes=info["nombreLentes"])

            lentes1.save()

            return render(request, "AppCoder/inicio.html")

    else: 
        
        formulario3 = LentesFormulario()

    return render(request, "AppCoder/LentesFormulario.html", {"form3":formulario3} )


def busquedaRelojes(request):

    return render (request, "AppCoder/busquedaRelojes.html")

def resultados(request):


    if request.GET["reloj"]:

        reloj = request.GET["reloj"]
        modelos = Relojes.objects.filter(modelo__icontains=reloj) # iexact para que muestre la busqueda

        return render(request, "AppCoder/resultados.html" , {"modelo":modelos, "reloj":reloj})

    else:

        respuesta = "No enviaste datos."

    
    return HttpResponse(respuesta)