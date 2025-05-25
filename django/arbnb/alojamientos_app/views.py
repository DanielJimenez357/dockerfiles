from django.shortcuts import render, redirect, get_object_or_404
from .models import Alojamiento, Alquiler
from .forms import AlojamientoForm, AlquilerForm, ComentarioAlquilerForm, RegistroUsuarioForm 

# Create your views here.

def alojamientos(request):
    alojamientos = Alojamiento.objects.filter(propietario=request.user.id)
    return render(request, 'alojamientos.html', {'alojamientos': alojamientos})


def editar_alojamiento(request, id):
    alojamiento_a_editar = get_object_or_404(Alojamiento, pk=id)
    if request.method == 'POST':
        form = AlojamientoForm(request.POST, instance=alojamiento_a_editar)
        if form.is_valid():
            form.save() 
            return redirect('alojamientos')
    else:
        form = AlojamientoForm(instance=alojamiento_a_editar)
    context = {
        'form': form,
        'alojamiento': alojamiento_a_editar 
    }
    return render(request, 'editar_alojamiento.html', context)

def nuevo_alojamiento(request):
    
    if request.method == "POST":
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            alojamiento = form.save(commit=False)
            alojamiento.propietario = request.user
            alojamiento.save()
            return redirect('alojamientos')
    else:
        form = AlojamientoForm()

    context = {
        'form': form,
    }

    return render(request, 'nuevo_alojamiento.html', context)

def ver_alquileres(request, id):

    alojamiento = get_object_or_404(Alojamiento, pk=id)

    alquileres = Alquiler.objects.filter(alojamiento = id)

    context = {
        'alquileres': alquileres,   
        'alojamiento': alojamiento
    }

    return render(request, 'alquileres.html', context)


def ver_alquilados(request):
    alquilados = Alquiler.objects.filter(cliente=request.user)
    context={
        'alquilados': alquilados,
    }
    return render(request, 'alquilar.html', context)


def alquilar(request):

    if request.method == "POST":
        form = AlquilerForm(request.POST)
        if form.is_valid():
            alquiler = form.save(commit=False)
            alquiler.cliente = request.user
            alquiler.save()
            return redirect('ver_alquilados')
    else:
        form = AlquilerForm()

    context = {
        'form': form
    }

    return render(request, 'alquilado.html', context)


def comentar(request, id):

    alquiler = get_object_or_404(Alquiler, pk=id)

    if request.method == "POST":
        form = ComentarioAlquilerForm(request.POST, instance=alquiler)
        if form.is_valid():
            form.save()
            return redirect('ver_alquilados')
    else:
        form = ComentarioAlquilerForm(instance=alquiler)

    context = {
        'form': form
    }

    return render(request, 'comentario.html', context)



def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})