from django.urls import path
from . import views


urlpatterns = [
    path("products/add/", views.add_products, name="addproducts"),
    path("products/view/", views.view_product, name="viewproducts"),
    path("products/edit/<int:id>", views.edit_product, name="editproduct"),
    path("products/unlist/<int:id>", views.unlist_product, name="unlist_product"),
    path("products/unlists/", views.view_unlist, name="unlist_products"),
    path("products/list/<int:id>", views.list_product, name="List_product"),
    path("products/variant/add/<int:id>", views.add_colour, name="addcolour"),
    path("products/variant/size/<int:id>", views.add_size, name="addsize"),    
    path("products/variant/<int:id>", views.product_variant, name="product_variant"),
    path("products/variant/edit/<int:id>", views.edit_variant, name="edit_variant"),
    path("products/variant/unlist/<int:id>", views.unlist_variant, name="unlist_variant"),
    path('products/variant/view/<int:product_id>/', views.unlisted_variants_view, name='unlisted_variants'),
    path("products/variant/list/<int:id>", views.list_variant, name="list_variant"),
]
