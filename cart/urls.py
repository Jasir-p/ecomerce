from django.urls import path
from .views import *


urlpatterns = [
    path("cart/add/<int:id>", AddCart.as_view(), name="add_cart"),
    path("cart/view/", Viewcart.as_view(), name="viewcart"),
    path("cart/update/", UpdateCartView.as_view(), name="update_cart"),
    path('cart/delete/<int:cart_id>', delete_cart, name="deletecart"),
    path("update-total/", cart_total_view, name="update_total"),
    path("checkout/", checkout, name="checkout"),
    path('coupons/add/',add_coupon,name='add-coupon'),
    path('check-address/edit/<int:address_id>',check_update_address,name="check-edit-address"),
    path('coupons/view/',view_admin_coupon,name="view-coupons"),
    path('check-address/add/',check_add_address,name="check-add-address"),

    path('coupons/edit/<int:id>/', edit_coupon, name='edit-coupon'),
    path('active-coupon/<int:id>',coupon_is_active,name='active-coupon')


]
