from django.core.exceptions import ValidationError


def check_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")
