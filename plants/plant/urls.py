from django.urls import path
from .views import plant_create, plant_details, plant_edit, plant_delete

urlpatterns = [
    path('create/', plant_create, name='plant-create'),
    path('details/<int:plant_id>/', plant_details, name='plant-details'),
    path('edit/<int:plant_id>/', plant_edit, name='plant-edit'),
    path('delete/<int:plant_id>/', plant_delete, name='plant-delete')
]
