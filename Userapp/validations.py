import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def validate_mobile_number(mobile_number):

    pattern = re.compile(r"^[6-9]\d{9}$")

    if pattern.match(mobile_number):
        return True
    else:
        return False