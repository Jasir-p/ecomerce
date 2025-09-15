from django.urls import path
from . import views

urlpatterns = [
    path("admin-login/", views.login, name="admin-login"),
    path("admin-dashboard/", views.dashbord, name="admin-dashboard"),
    path("user/details/", views.view_user, name="user-details"),
    path("category/", views.category, name="category"),
    path("brands/add", views.brand, name="brands_add"),
    path("view-category/", views.view_category, name="view-category"),
    path("admin-logout/", views.logout, name="admin-logout"),
    path("brands/view/", views.view_brands, name="view_brands"),
    path("DelCategory/<int:ca_id>", views.category_unlist, name="delcategory"),
    path("ViewUnlistCategory/", views.unlist_categories, name="unlistcategory"),
    path("EditCategory/<int:ca_id>", views.edit_category, name="EditCatogory"),
    path("ListCategory/<int:ca_id>", views.list_category, name="listcategory"),
    path("BlockUser/<int:u_id>", views.block_user, name="blockuser"),
    path("UnblockUser/<int:u_id>", views.unblock_user, name="unblockuser"),
    path("brands/unlist/<int:b_id>", views.unlist_brand, name="unlist_brand"),
    path("brands/unlist/view/", views.viewunlist_brands, name="view_unlist_brand"),
    path("brands/list/<int:b_id>", views.list_brand, name="list_brands"),
    path("brands/edit/<int:id>", views.edit_brand, name="edit_brands"),
    # path("Salesreport/",views.sales_report,name="sales_report"),
     path('download-sales-report/', views.download_sales_report, name='download_sales_report'),
]
