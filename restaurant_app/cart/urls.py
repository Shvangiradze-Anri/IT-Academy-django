from django.urls import path
from .views import cart, add_to_cart, increase_quantity, decrease_quantity, delete_cart

urlpatterns = [
    path("", cart, name="cart"),
    path("add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("increase/<int:cart_id>/", increase_quantity, name="increase"),
    path("decrease/<int:cart_id>/", decrease_quantity, name="decrease"),
    path("delete/<int:cart_id>/", delete_cart, name="delete_cart"),
]