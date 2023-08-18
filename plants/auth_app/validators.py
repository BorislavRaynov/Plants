from django.core.exceptions import ValidationError


def check_starts_capital(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')