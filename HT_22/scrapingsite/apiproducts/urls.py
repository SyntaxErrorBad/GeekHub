from django.urls import path
from django.urls import include
from .views import ProductListAPIView, ProductsCategoriesListAPIView, ProductInfoListAPIView, ProductAddProductAPIView
from .views import LoginUserAPIView, LogoutUserAPIView
from .views import ShoppingCartAddItemAPIView, ShoppingCartRemoveItemAPIView
from .views import ShoppingCartRemoveQuantityItemAPIView, ShoppingCartAddQuantityItemAPIView
from .views import ShoppingCartClearAPIView

from .views import ShoppingCartAddOrRemoveItemAPIView

app_name = 'api'

shopping_cart = [
    path('', ShoppingCartAddOrRemoveItemAPIView.as_view(), name="shopping-cart"),
    path('add/', ShoppingCartAddItemAPIView.as_view(), name='shopping-cart-add-api'),
    path('remove/', ShoppingCartRemoveItemAPIView.as_view(), name='shopping-cart-remove-api'),
    path('clear/', ShoppingCartClearAPIView.as_view(), name='shopping-cart-clear'),
    path('add/quantity/', ShoppingCartAddQuantityItemAPIView.as_view(), name='shopping-cart-add-quantity-api'),
    path('remove/quantity/', ShoppingCartRemoveQuantityItemAPIView.as_view(), name='shopping-cart-remove-quantity-api'),
]

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list-json'),
    path('products-categories/', ProductsCategoriesListAPIView.as_view(), name='product-categorys-list-json'),
    path('product-info/<str:product_id>/', ProductInfoListAPIView.as_view(), name='product-info-list-json'),
    path('product-add/', ProductAddProductAPIView.as_view(), name='product-add'),
    path('login/', LoginUserAPIView.as_view(), name='login-user-api'),
    path('logout/', LogoutUserAPIView.as_view(), name='logout-user-api'),
    path('shopping-cart/', include(shopping_cart))
]
