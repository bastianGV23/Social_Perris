from django import forms
from .models import Adopcion
class formAdopcion(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = [
            'rut',
            'id_perro',
            'id_estado',
        ]
        widgets = {
            'rut': forms.Select(attrs={'class':'form-control col-10'}),
            'id_perro': forms.Select(attrs={'class':'form-control col-10'}),
            'id_estado': forms.Select(attrs={'class':'form-control col-10'}),
        }
        labels = {
            'rut': 'Rut del dueño',
            'id_perro': 'ID de la mascota',
        }
class formAdopcion2(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = [
            'rut',
            'id_perro',
            'id_estado',
        ]
        widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
            'id_perro': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
            'id_estado': forms.Select(attrs={'class':'form-control col-10'}),
        }
        labels = {
            'rut': 'Rut del dueño',
            'id_perro': 'ID de la mascota',
        }
