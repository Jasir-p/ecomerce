from django.urls import path
from .views import *


urlpatterns = [
    path("offer/add/",add_offer,name="add_offer"),
    path('offer/view/',view_offers,name="view_offer"),
    path('offer/edit/<int:offer_id>',edit_offer,name="edit_offer"),
    path("toggle-offer/<int:id>",active_section,name="toggle_offer"),
]
