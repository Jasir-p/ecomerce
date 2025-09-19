from django.urls import path
from . import views

urlpatterns = [
    path("admin-login/", views.login, name="admin-login"),
    path("admin-dashboard/", views.dashbord, name="admin-dashboard"),
    path("user/details/", views.view_user, name="user-details"),
    path("category/", views.category, name="category"),
    path("brands/add/", views.brand, name="brands_add"),
    path("view-category/", views.view_category, name="view-category"),
    path("admin-logout/", views.logout, name="admin-logout"),
    path("brands/view/", views.view_brands, name="view_brands"),
    path("categories/<int:ca_id>/delete/", views.category_unlist, name="category-delete"),
    path("categories/unlisted/", views.unlist_categories, name="categories-unlisted"),
    path("categories/<int:ca_id>/edit/", views.edit_category, name="category-edit"),
    path("categories/<int:ca_id>/list/", views.list_category, name="category-list"),
    path("users/<int:u_id>/block/", views.block_user, name="user-block"),
    path("users/<int:u_id>/unblock/", views.unblock_user, name="user-unblock"),
    path("brands/unlist/<int:b_id>", views.unlist_brand, name="unlist_brand"),
    path("brands/unlist/view/", views.viewunlist_brands, name="view_unlist_brand"),
    path("brands/list/<int:b_id>", views.list_brand, name="list_brands"),
    path("brands/edit/<int:id>", views.edit_brand, name="edit_brands"),
    # path("Salesreport/",views.sales_report,name="sales_report"),
     path('download-sales-report/', views.download_sales_report, name='download_sales_report'),
]
