from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name="Inicio" ),
    path("relojes/", relojes, name = "Relojes"),
    path("billeteras/", billeteras, name = "Billeteras"),
    path("lentes/", lentes, name ="Lentes"),
    path("relojesFormulario/", relojesFormulario, name = "formularioRelojes" ),
    path("billeterasFormulario/", billeterasFormulario, name = "formularioBilleteras" ),
    path("lentesFormulario/", lentesFormulario, name = "formularioLentes" ),
    path("buscarRelojes/", busquedaRelojes, name="BuscarRelojes" ),
    path("resultados/", resultados, name = "ResultadosBusqueda"),


]
