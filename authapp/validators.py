from django.core.exceptions import ValidationError


def minNameLength(value):
    if len(value) < 5:
        raise ValidationError('Введенные данные должны содержать не меньше 5 символов.')
