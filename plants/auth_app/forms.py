from django import forms
from .models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['picture']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }

class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'picture': 'Profile Picture',
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }

class DeleteProfileForm(BaseProfileForm):
    pass
