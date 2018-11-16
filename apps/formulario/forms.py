from django import forms

from apps.formulario.models import Contacto

class Formulario(forms.ModelForm):
    
    class Meta:
        model = Contacto

        fields = [
            'nombres',
            'apPaterno',
            'apMaterno',
            'rut',
            'dvRut',
            'fNacimiento',
            'correo',
            'telefono',
        ]
        labels = {
            'nombres': 'Nombres',
            'apPaterno': 'Apellido paterno',
            'apMaterno': 'Apellido materno',
            'rut': 'Rut',
            'dvRut': 'DV RUT',
            'fNacimiento': 'Fecha de nacimiento',
            'correo': 'E-MAIL',
            'telefono': 'Telefono',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apPaterno': forms.TextInput(attrs={'class':'form-control'}),
            'apMaterno': forms.TextInput(attrs={'class':'form-control'}),
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'dvRut': forms.TextInput(attrs={'class':'form-control'}),
            'fNacimiento': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
        }

        