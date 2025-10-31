from django.urls import path
from .views import Placed_order, order_management, order_details, Confirm, status,retry_payment

urlpatterns = [
    path("placeorder/", Placed_order, name="placed_order"),
    path("order-management/", order_management, name="order_management"),
    path("order-details/<int:id>", order_details, name="order_details"),
    path("Confirm/", Confirm, name="confirm"),
    path("update-status/<int:id>", status, name="update_status"),
    path("retry-amount/<int:id>",retry_payment,name="retry_payment")
  
   
    

]
