from django.shortcuts import render,redirect
from .models import perrito
from apps.rescate.forms import formServicio
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def lista_rescate(request):
    rescata = perrito.objects.all()
    return render(request, "rescate/rescate.html",{'rescata':rescata})
@login_required
def crea_rescate(request):
    form = formServicio(request.POST, request.FILES or None)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
        form = formServicio()
    context =  {
        'form': form,
    }
    return render(request,'rescate/nuevo.html',context)
@login_required
def edita_rescate(request,id_perrito):
    perro = perrito.objects.get(id = id_perrito)
    if request.method == 'GET':
        form = formServicio(instance=perro)
    else:
        form = formServicio(request.POST, request.FILES or None, instance=perro)
        if form.is_valid():
            form.save()
        return redirect('rescate:ver')
    return render(request,'rescate/edita.html',{'form':form})
@login_required
def elimina_rescate(request,id_perrito):
    perro = perrito.objects.get(id = id_perrito)
    if request.method == 'POST':
        perro.delete()
        return redirect('rescate:ver')
    return render(request,'rescate/elimina.html',{'perro':perro})
        
