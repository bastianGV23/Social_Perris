from django import forms

from apps.rescate.models import perrito

class formServicio(forms.ModelForm):
    class Meta:
        model = perrito
        fields = [
            'nombrePerro',
            'razaP',
            'descripcion',
            'imagen',
        ]
        widgets = {
            'nombrePerro': forms.TextInput(attrs={'class':'form-control col-10'}),
            'razaP': forms.TextInput(attrs={'class':'form-control col-10'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control col-10'}),
        }
        labels = {
            'nombrePerro': 'Nombres',
            'razaP': 'Raza del perro',
            'descripcion': 'Descripcion',
            'imagen': 'Imagen',
        }


        