from django.urls import path
from . import views
from .views import*


urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("", views.user_home, name="user_home"),
    path("user/signup/", views.user_signup, name="SignUp"),
    path("otp", views.otp, name="otp"),
    path("resend-otp/", views.resend_otp, name="resend"),
    path("user/logout/", views.logout, name="userlogout"),
    path("shop/", views.shop, name="shop"),
    path("shop/details/<int:p_id>", views.shopdetails, name="shopdetails"),
    path("filterd/", views.filterd, name="filterd"),
    path("user/address/add/", views.add_address, name="add_address"),
    path("user/address/view/", views.view_address, name="view_address"),
    path("user/address/edit/<int:address_id>",views.update_address,name="edit_adress"),
    path("user/address/delete/<int:address_id>", views.delete_address, name="delete_address"),
    path("user/wishlists/", views.wish_list, name="wishlist"),
    path("user/wishlists/add/<int:product_id>", views.add_to_wishlist, name="addwishlist"),
    path("user/wishlists/remove/<int:id>", views.Remove_wishlist, name="wishlist_remove"),
    path("user/change-password/", views.change_password, name="changepassword"),
    path("user/order/", views.user_order, name="user_order"),
    path(
        "user/order/detail/<int:id>", views.view_order_details, name="view_order_details"
    ),
    path("user/order/detail/tracking/<int:id>", views.order_track, name="order_track"),
    path("error/", views.error_page, name="error"),
    path("request-cancel/<int:id>", views.request_status_cancel, name="request_cancel"),
    path("request-return/<int:id>", views.request_status_return, name="request_return"),
    path("user/wallet/",views.wallet,name="wallet"),
    path("user/wallet/add/,",views.add_to_wallet,name="add_to_wallet"),
    path('user/coupon/',views.view_coupons,name="view_coupon"),
    path('api/products/<int:product_id>/sizes', views.get_product_sizes, name='get_sizes'),
    path('wishlist-to-cart/<int:id>/<int:size_id>/', views.wishlist_to_cart, name='wishlist_to_cart'),
    path("user/refarel/",views.myrefrals,name='my_refarel'),
    path("search/",views.search_shop,name="search"),
    path("user/forgot/password/",views.forgot_email,name='f_password'),
    path('user/otp-password/',views.check_otp,name="otp_password"),
    path('user/resend/otp-password/',views.resend_otp_password,name="resend_otp_password"),
    path("user/password/",views.set_password,name='password_section'),
    path('invoice/<int:order_id>/', views.generate_invoice, name='generate_invoice'),
    path('user/add-number/',views.add_phone,name="add_number"),
]
