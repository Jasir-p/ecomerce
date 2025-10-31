
from .models import Product
from django.core.files.uploadedfile import UploadedFile
from PIL import Image

def is_valid_image(file):
    # Check if the file is an image
    if not isinstance(file, UploadedFile):
        return False

    try:

        Image.open(file)
        return True
    except Exception as e:

        return False


def product_form_validations(name,price,thumbnail,product_id=None,isImage=True):
    if Product.objects.filter(name__iexact=name).exists():
        return "product already exist"
    if not name or not name[0].isalpha():
        return "Field must start with a character"
    if len(name) < 2:
        return  "Field must atleast two character"

    elif int(price) < 0:
        return "price must be postive number"
    elif not is_valid_image(thumbnail):
        return "Thumbnail is an invalid image file "
    

    return None
    


