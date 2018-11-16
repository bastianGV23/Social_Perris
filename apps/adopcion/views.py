from django.shortcuts import render,redirect,HttpResponse
from .models import Adopcion
from .forms import formAdopcion,formAdopcion2
from apps.rescate.models import Estado
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def lista_adopcion(request):
    adopta = Adopcion.objects.all()
    return render(request, "adopcion/ver.html",{'adopta':adopta})
@login_required
def asignar_adopcion(request):
    form = formAdopcion(request.POST)
    if form.is_valid():
      form.save()
      return redirect('adopcion:ver')
    context =  {
        'form': form,
    }
    return render(request,'adopcion/nueva.html',context)
@login_required
def adopta_perro(request,id_adopcion):  
    adop = Adopcion.objects.get(id = id_adopcion)
    if request.method == 'GET':
        form = formAdopcion2(instance=adop)
    else:
        form = formAdopcion2(request.POST, instance=adop)
        if form.is_valid():
            form.save()
        return redirect('adopcion:ver')
    context =  {
        'form': form,
        'adop':adop,
    }
    return render(request,'adopcion/adopta.html',context)