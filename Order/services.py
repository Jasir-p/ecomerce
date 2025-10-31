from Products.models import size_variant
from .models import Order
import secrets
import string



def generate_order_id(length=8):

    digits = string.digits

    first_two_chars = "OID"

    remaining_chars = "".join(secrets.choice(digits) for i in range(length - 3))

    order_id = first_two_chars + remaining_chars
    while Order.objects.filter(order_id=order_id).exists():
        remaining_chars = "".join(secrets.choice(digits) for i in range(length - 3))
        order_id = first_two_chars + remaining_chars

    return order_id



def check_is_available(size_id,quantity_ordered):
    item_size = size_variant.objects.get(id=size_id)
    if item_size.quantity < quantity_ordered:
        return f"Sorry, '{item_size.Color_products}' is out of stock."



def create_order(user,address,cart,payment,payment_mode,total_amount):
    return  Order.objects.create(
                    user=user,
                    total_amount=total_amount,
                    payment = payment,
                    payment_method=payment_mode,
                    coupon_id=cart.coupon.code if cart.coupon else None,
                    coupon_amount=cart.coupon.discount_amount if cart.coupon else None,
                    min_amount=cart.coupon.min_amount if cart.coupon else None,
                    shipping_charge=cart.shipping_charge,
                    order_id=generate_order_id(),
                    name=address.name,
                    address=address.address,
                    House_no=address.House_no,
                    city=address.city,
                    state=address.state,
                    country=address.country,
                ) 


def create_order_items():
    return 