from django import template
from plants.auth_app.models import Profile

register = template.Library()

@register.simple_tag
def find_profile():
    return Profile.objects.first()
