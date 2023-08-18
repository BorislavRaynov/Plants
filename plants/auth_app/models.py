from django.db import models
from django.core.validators import MinLengthValidator
from .validators import check_starts_capital
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)], blank=False, null=False)
    first_name = models.CharField(max_length=10, validators=[check_starts_capital], blank=False, null=False)
    last_name = models.CharField(max_length=10, validators=[check_starts_capital], blank=False, null=False)
    picture = models.URLField(blank=True, null=True)
