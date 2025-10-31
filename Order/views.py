from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from cart.models import *
from cart.urls import *
from Admin.urls import *
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login as log, logout as authlogout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_control

from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from Userapp.models import CustomUser,Wallet,Wallet_transaction
from Userapp.urls import *
from django.utils.translation import gettext as _
import uuid
from django.db.models import F
import random
import time
import secrets
import string
import razorpay
from django.conf import settings
from django.urls import reverse
from .services import check_is_available,create_order

# Create your views here.
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
def initiate_payment(items):
    data = {
        "currency": "INR",
        "payment_capture": "1",
        "amount": items[0]["amount"] * 100,
    }

    razorpay_order = razorpay_client.order.create(data=data)
    razorpay_order_id = razorpay_order["id"]
    for item in items:
        item_data = {
            "amount": item["amount"] * 100,
            "currency": "INR",
        }
    razorpay_client.order.create(data=item_data)
    return razorpay_order_id


def Placed_order(request):
    try:
        if request.method == "POST":
            print("checking")
            try:
                address_id = request.POST.get("address")
                selected_address = Address.objects.get(id=address_id)
                
            except:
                messages.error(request,"please select a address")
                return redirect("checkout")
            payment_mode = request.POST.get("payment_method")
            print(payment_mode)
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart__user=request.user)
            total_amount = cart.Totel()
            if payment_mode == 'Cash On Delivery':  
                payment = Payment.objects.create(
                    user=request.user, method=payment_mode, amount=total_amount
                )
                order = create_order(request.user,selected_address,cart,payment,payment_mode,total_amount)
                order.payment = payment
                order.save()

                for cart_item in CartItem.objects.filter(cart=cart):
                    product = cart_item.product
                    prod = Color_products.objects.get(id=product.id)
                    quantity_ordered = cart_item.quantity
                    
                    if prod.product.offer_price  is not None:
                       prices = prod.product.offer_price
                    else:
                        prices = prod.product.price
                    
                    size = cart_item.product_size_color.id
                    product_size_colors = size_variant.objects.get(id=size)
                    is_quantity_available = check_is_available(size,quantity_ordered)

                    if  is_quantity_available or prod.is_listed == False:
                        order.delete()
                        payment.delete()
                        messages.error(
                            request, is_quantity_available
                        )
                        return redirect("viewcart")
                   
                    product_size_colors.quantity = F("quantity") - quantity_ordered
                    product_size_colors.save()
                    
                    OrderProduct.objects.create(
                        order=order,
                        product=prod,
                        price=prices,
                        quantity=quantity_ordered,
                        size=product_size_colors,
                        status= 'Processing',
                        trackig_id=generate_tracking_id(),
                    )
                order.save()
                cart_items.delete()
                cart.delete()
                
                return render(request, "confirm.html",{'order':order})

            
            elif payment_mode == "Razorpay":

                
                payment_status = request.POST.get('payment_status')
                failure_reason = request.POST.get('failure_reason')
                payment_failed=True if payment_status =="failed" else False
                
                total_amount = cart.Totel()
                if payment_status == "success":
                    items = [
                        {
                            "amount": int(total_amount) * 100,
                        }
                    ]
                    order_id = initiate_payment(items)
                    if order_id is None:
                        messages.error(request, "Payment initiation failed. Please try again.")
                        return redirect("checkout")
                
                    payment = Payment.objects.create(   
                        user=request.user, method=payment_mode, amount=total_amount,Transaction_id=order_id, status=payment_status 
                    )
                else:
                    payment = Payment.objects.create(   
                        user=request.user, method=payment_mode, amount=total_amount, status=payment_status 
                    )            
                order = create_order(request.user,selected_address,cart,payment,payment_mode,total_amount)
                for cart_item in CartItem.objects.filter(cart=cart):
                    product = cart_item.product
                    prod = Color_products.objects.get(id=product.id)
                    quantity_ordered = cart_item.quantity
                    size = cart_item.product_size_color.id
                    if prod.product.offer_price  is not None :
                       prices = prod.product.offer_price
                    else:
                        prices = prod.product.price

                    product_size_colors = size_variant.objects.get(id=size)
                    is_quantity_available = check_is_available(size,quantity_ordered)

                    if  is_quantity_available or prod.is_listed == False:
                        order.delete()
                        payment.delete()
                        messages.error(
                            request, is_quantity_available
                        )
                        return redirect("viewcart")
                    
                    product_size_colors.quantity = F("quantity") - quantity_ordered
                    product_size_colors.save()
                    OrderProduct.objects.create(
                        order=order,
                        product=prod,
                        quantity=quantity_ordered,
                        price=prices,
                        status='Processing' if not payment_failed else 'Pending',
                        size=product_size_colors,
                        trackig_id=generate_tracking_id(),
                    )

                order.save()
                cart_items.delete()
                cart.delete()
                print("ordersave")
                return render(request, "confirm.html",{'payment_failed': payment_failed,'order':order})
            
            elif payment_mode == "Wallet":
                print('checking wallet')                
                wallet=Wallet.objects.get(user=request.user)
                wallet_user, created = Wallet.objects.get_or_create(user=request.user)                              
                total_amount = cart.Totel()
                if wallet.balance >= total_amount:
                    wallet_user.balance -= total_amount
                    payment = Payment.objects.create(   
                            user=request.user, method=payment_mode, amount=total_amount, status='success' 
                        )
                    order = create_order(request.user,selected_address,cart,payment,payment_mode,total_amount)

                    for cart_item in CartItem.objects.filter(cart=cart):
                        product = cart_item.product
                        prod = Color_products.objects.get(id=product.id)
                        quantity_ordered = cart_item.quantity
                        size = cart_item.product_size_color.id
                        if prod.product.offer_price  is not None :
                            prices = prod.product.offer_price
                        else:
                            prices = prod.product.price

                        
                        product_size_colors = size_variant.objects.get(id=size)

                        is_quantity_available = check_is_available(size,quantity_ordered)

                        if  is_quantity_available or prod.is_listed == False:
                            order.delete()
                            payment.delete()
                            messages.error(
                                request, is_quantity_available
                            )
                            return redirect("viewcart")
                        
                        product_size_colors.quantity = F("quantity") - quantity_ordered
                        product_size_colors.save()
                        order_item=OrderProduct(
                            order=order,
                            product=prod,
                            quantity=quantity_ordered,
                            price=prices,
                            status='Processing',
                            size=product_size_colors,
                            trackig_id=generate_tracking_id(),
                        )
                        transaction_id = str(uuid.uuid4())
                        Wallet_transaction.objects.create(
                        wallet=wallet_user,
                        transaction_id=transaction_id,
                        money_withdrawn=total_amount

                        )
                        order_item.save()
                        order.save()
                        wallet_user.save()
                        
                    order.save()
                    cart_items.delete()
                    cart.delete()
                    print("ordersave")
                    
                    return render(request, "confirm.html",{'order':order})
                messages.error(request,'Wallet has insufficient funds')
        
            return redirect("checkout")
    except Exception as e :
        print(str(e))
        
        messages.error(request,e)
        return redirect("checkout")
       
        
# def check_and_update(cart_item):

def generate_tracking_id():
    fixed_chars = "HP"
    max_unique_id_length = 20 - len(fixed_chars)
    unique_id = str(int(time.time())) + str(random.randint(10000, 99999))
    unique_id = unique_id[:max_unique_id_length]
    tracking_id = fixed_chars + unique_id
    return tracking_id


# Generate a tracking ID

@never_cache
@login_required(login_url="adminlogin")
def order_management(request):

    if request.user.is_superuser:
        data = Order.objects.all().order_by('-id')
        return render(request, "Order_management.html", {"data": data})
    return redirect("adminlogin")


@never_cache
@login_required(login_url="adminlogin")
def order_details(request, id):
    if request.user.is_superuser:
        data = OrderProduct.objects.filter(order__id=id)
        order = Order.objects.get(id=id)
        order_products = OrderProduct.objects.filter(order__id=id).exclude(status__in=['Cancelled', 'Returned'])
        order_item_count = True if order_products.count()> 0 else False
   
        totel_amount=order_products.annotate(totel_price=F('quantity')* F('price')).aggregate(totel_sum=Sum('totel_price'))['totel_sum'] or 0
        

        return render(request, "order_items.html", {"data": data, "Address": order,
                                                    'totel_amount':totel_amount,'is_item_count':order_item_count})
    return redirect("adminlogin")


@never_cache
def Confirm(request):

    return render(request, "confirm.html")

def status(request, id):
    if request.method == "POST":
        get_status = request.POST.get("status")
        

        item = get_object_or_404(OrderProduct, id=id)
        order = item.order
        size = get_object_or_404(size_variant, id=item.size.pk)
        payment = get_object_or_404(Payment, pk=item.order.payment.pk)
        

        if get_status in ['Cancelled', 'Returned']:
            with transaction.atomic():
                
                size.quantity += item.quantity
                
                

                item_total = item.quantity * item.price

                Quantity = OrderProduct.objects.filter(order__id=order.id).exclude(status__in=['Cancelled', 'Returned']).count() == 1

                shipping=50 if order.shipping_charge else 0

                if order.payment_method == "Razorpay" or order.payment_method == "Wallet" or get_status=='Returned':
                    wallet = get_object_or_404(Wallet, user=order.user)
                    if payment.status=="success":
                        if Quantity:
                            
                            refund_amount = order.total_amount
                            order.total_amount =0
                            # payment.amount=0
                            payment.status="Cancelled"
                            if order.coupon_id:
                                coupon = get_object_or_404(Coupon, code=order.coupon_id)
                                order.coupon_id=None
                                CustomerCoupon.objects.get(user=order.user,coupon__id=coupon.pk).delete()
                        else:
                            reduandant_amount=order.total_amount-item_total
                            order.total_amount -= item_total
                            payment.amount-=item_total
                            shipping_charge_add = 50 if reduandant_amount-shipping<3000 else 0
                            

                            if order.coupon_id:
                                coupon = get_object_or_404(Coupon, code=order.coupon_id)
                                
                                
                                
                                if order.total_amount -shipping < order.min_amount:
                                    order.coupon_id=None
                                    refund_amount = item_total - order.coupon_amount
                                    order.total_amount +=  order.coupon_amount
                                    payment.amount+=item_total
                                
                                    CustomerCoupon.objects.get(user=order.user,coupon__id=coupon.pk).delete()
                                else:
                                    refund_amount = item_total
                            else:
                                refund_amount = item_total
                            
                            if shipping_charge_add and not shipping:
                                refund_amount = item_total- shipping_charge_add
                                order.shipping_charge=True
                            
                        wallet.balance += refund_amount
                        transaction_id = str(uuid.uuid4())


                        Wallet_transaction.objects.create(
                            wallet=wallet,
                            transaction_id=transaction_id,
                            money_deposit=refund_amount
                        )
                        wallet.save()
                        
                        
                    else:
                        if Quantity:
                        
                            refund_amount = order.total_amount
                            # order.total_amount =0
                            payment.amount=0
                            payment.status="Cancelled"
                            if order.coupon_id:

                                coupon = get_object_or_404(Coupon, code=order.coupon_id)
                                CustomerCoupon.objects.get(user=order.user,coupon__id=coupon.pk).delete()
                                order.coupon_id=None
                        else:
                            order.total_amount -= item_total
                            payment.amount-=item_total
                            if order.coupon_id:
                                coupon = get_object_or_404(Coupon, code=order.coupon_id)
                                if order.total_amount < order.min_amount:
                                    refund_amount = item_total - order.coupon_amount
                                    order.total_amount +=  order.coupon_amount
                                    payment.amount+=item_total
                                    
                                    CustomerCoupon.objects.get(user=order.user,coupon__id=coupon.pk).delete()
                                    order.coupon_id=None
                                    
                                    payment.amount-=order.total_amount

                    order.save()
                    payment.save()
                    item.status = get_status
                    size.save()
                    item.save()
                   
        
                
        else:
            if get_status =='Delivered':
                payment.status="success"
                payment.save()     
            item.status = get_status
            item.save()
        
            

        return redirect("order_details", item.order.id)


def generate_short_uuid():
    uuid_str = str(uuid.uuid4())
    
    truncated_uuid = uuid_str[:8]  
    return truncated_uuid

def retry_payment(request,id):
    
        order=Order.objects.get(id=id)
        payment=Payment.objects.get(id=order.payment.pk)
        amount=int(order.total_amount)
        trans_id=razar_payment(amount)

        if  trans_id is not None:
            payment.status="success"
            payment.Transaction_id=trans_id
            OrderProduct.objects.filter(order__id=order.id).update(status='Processing')
            payment.save()
        return redirect('user_order')

def razar_payment(items):
    data = {
        "currency": "INR",
        "payment_capture": "1",
        "amount": items * 100,
    }

    razorpay_order = razorpay_client.order.create(data=data)
    razorpay_order_id = razorpay_order["id"]
    
    item_data = {
            "amount": items * 100,
            "currency": "INR",
        }
    razorpay_client.order.create(data=item_data)
    return razorpay_order_id
