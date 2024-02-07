from django.urls import path
from . import views

urlpatterns = [
    path('change-info-product/<str:product_id>/', views.change_info_product, name='changeinfoproduct'),
]