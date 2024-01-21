from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_products, name='add_products'),
    path('my-products/', views.my_products, name='my_products'),
    path('product/<str:product_id>/', views.product_detail, name='product_detail'),
    path('exeption/', views.exeption_page, name="exeption_page"),
]
