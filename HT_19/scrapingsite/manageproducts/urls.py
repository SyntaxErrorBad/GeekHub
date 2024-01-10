from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_products, name='add_products'),
    path('my-products/', views.my_products, name='my_products'),
    path('product/<str:product_id>/', views.product_detail, name='product_detail'),
    path('exeption/', views.exeption_page, name="exeption_page"),
    path('shopping-cart-add-item/<str:product_id>/', views.shopping_cart_add_item, name="shopping_cart_add_item"),
    path('shopping-cart-remove-item/<str:product_id>/', views.shopping_cart_remove_item,
         name="shopping_cart_remove_item"),
    path('shopping-cart', views.shopping_cart_page, name="shopping_cart_page"),
    path("shopping-cart-clear", views.shopping_cart_clear, name="clear_all_cart")
]
