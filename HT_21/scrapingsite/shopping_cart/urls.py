from django.urls import path
from . import views

urlpatterns = [
    path('shopping-cart-add-item/<str:product_id>/', views.shopping_cart_add_item, name="shopping_cart_add_item"),
    path('shopping-cart-remove-item/<str:product_id>/', views.shopping_cart_remove_item,
         name="shopping_cart_remove_item"),
    path('shopping-cart', views.shopping_cart_page, name="shopping_cart_page"),
    path("shopping-cart-clear", views.shopping_cart_clear, name="clear_all_cart"),
    path('shopping-cart-manipulate-item', views.shopping_cart_manipulate_one_item,
         name='shopping_cart_manipulate_one_item'),
]