import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import CustomUser

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
    


def user_validation(username,email,number,password):

    if CustomUser.objects.filter(username=username).exists():
        return  "The username is already taken"

    elif not username.strip():
        return "The username is not valid"

    elif CustomUser.objects.filter(email=email).exists():
        return "The email is already taken"
    elif not is_valid_email(email):
        return "The email is not valid"
    
    elif not validate_mobile_number(number):
        return "The Mobail number is not valid"
    elif len(password) < 6:
        return "The password should be at least 6 characters"

    elif not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    
    elif not any(char.islower() for char in password):  # Corrected condition
        return  "Password must contain at least one lowercase letter"
    
    elif not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    

    return None