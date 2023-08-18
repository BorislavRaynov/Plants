from django.shortcuts import render, redirect
from .forms import CreatePlantForm, EditPlantForm, DeletePlantForm
from .models import Plant
# Create your views here.
# plant_create, plant_details, plant_edit, plant_delete


def plant_create(request):
    form = CreatePlantForm()

    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'plants/plant/create-plant.html', context=context)


def plant_details(request, plant_id):
    plant = Plant.objects.filter(id=plant_id).get()

    context = {
        'plant': plant
    }

    return render(request, 'plants/plant/plant-details.html', context=context)


def plant_edit(request, plant_id):
    plant = Plant.objects.filter(id=plant_id).get()
    form = EditPlantForm(instance=plant)

    if request.method == 'POST':
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }

    return render(request, 'plants/plant/edit-plant.html', context=context)

def plant_delete(request, plant_id):
    plant = Plant.objects.filter(id=plant_id).get()
    form = DeletePlantForm(instance=plant)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')


    context = {
        'plant': plant,
        'form': form
    }

    return render(request, 'plants/plant/delete-plant.html', context=context)

