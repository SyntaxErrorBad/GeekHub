from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic_page, name='basic_page'),
    path('add/', views.add_products, name='add_products'),
    path('my-products/', views.my_products, name='my_products'),
    path('product/<str:product_id>/', views.product_detail, name='product_detail'),
    path('exeption/', views.exeption_page, name='exeption_page'),
    path('category/<str:category>/', views.category_page, name='category_product')
]
