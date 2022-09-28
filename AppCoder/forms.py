from django import forms

class RelojesFormulario(forms.Form):

    reloj = forms.CharField()
    modelo = forms.IntegerField()

class LentesFormulario(forms.Form):

    nombreLentes = forms.CharField()

class BilleterasFormulario(forms.Form):

    nombreBilleteras = forms.CharField()