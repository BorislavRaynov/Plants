from django.db import models
from django.core.validators import MinLengthValidator
from .validators import check_only_letters


# Create your models here.
class Plant(models.Model):
    CHOISES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants')
    )

    type = models.CharField(
        max_length=14,
        choices=CHOISES,
        blank=False,
        null=False
    )

    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), check_only_letters],
        blank=False,
        null=False
    )

    image = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

