from django.shortcuts import render,redirect
from apps.formulario.forms import Formulario
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required  
def formulario_view(request):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('index')
    else:
        form = Formulario()
    
    return render(request, 'formulario/contacto.html',{'form':form})