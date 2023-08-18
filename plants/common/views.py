from django.shortcuts import render, redirect
from plants.plant.models import Plant


# Create your views here.
# home_page, catalogue

def home_page(request):
    return render(request, 'plants/common/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants
    }

    return render(request, 'plants/common/catalogue.html', context=context)

