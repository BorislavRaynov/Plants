from django.shortcuts import render, redirect
from plants.plant.models import Plant
from .models import Profile
from .forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
# Create your views here.

def create_profile(request):
    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'plants/auth_app/create-profile.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'plants/auth_app/edit-profile.html', context=context)

def details_profile(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'plants': Plant.objects.all()
    }

    return render(request, 'plants/auth_app/profile-details.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()
    if request.method == 'POST':
        plants.delete()
        profile.delete()
        return redirect('home-page')

    return render(request, 'plants/auth_app/delete-profile.html')
