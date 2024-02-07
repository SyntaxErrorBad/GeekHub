from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart_page, name="shopping_cart_page"),
    path('add-item/<str:product_id>/', views.shopping_cart_add_item, name="shopping_cart_add_item"),
    path('remove-item/<str:product_id>/', views.shopping_cart_remove_item, name="shopping_cart_remove_item"),
    path("clear/", views.shopping_cart_clear, name="clear_all_cart"),
    path('manipulate-item/', views.shopping_cart_manipulate_one_item, name='shopping_cart_manipulate_one_item'),
]