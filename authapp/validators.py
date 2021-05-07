from django.core.exceptions import ValidationError


def minNameLength(value):
    if len(value) < 5:
        raise ValidationError('The user name must contain at least 5 characters')
