from django import forms
from .models import Plant


class BasePlantForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'image': 'Image URL'
        }


class CreatePlantForm(BasePlantForm):
    pass

class EditPlantForm(BasePlantForm):
    pass

class DeletePlantForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
