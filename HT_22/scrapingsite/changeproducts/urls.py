from django.urls import path
from . import views

urlpatterns = [
    path('changeinfoproduct/<str:product_id>/', views.change_info_product, name='changeinfoproduct'),
]