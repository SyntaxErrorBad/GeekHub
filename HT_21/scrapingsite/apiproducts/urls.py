from django.urls import path
from .views import ProductListAPIView, ProductsCategoriesListAPIView, ProductInfoListAPIView, ProductAddProductAPIView
from .views import LoginUserAPIView, LogoutUserAPIView
from .views import ShoppingCartAddItemAPIView, ShoppingCartRemoveItemAPIView
from .views import ShoppingCartRemoveQuantityItemAPIView, ShoppingCartAddQuantityItemAPIView
from .views import ShoppingCartClearAPIView


urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list-json'),
    path('products-categories/', ProductsCategoriesListAPIView.as_view(), name='product-categorys-list-json'),
    path('product-info/<str:product_id>/', ProductInfoListAPIView.as_view(), name='product-info-list-json'),
    path('product-add/', ProductAddProductAPIView.as_view(), name='product-add'),
    path('login/', LoginUserAPIView.as_view(), name='login-user-api'),
    path('logout/', LogoutUserAPIView.as_view(), name='logout-user-api'),
    path('shopping-cart-add/', ShoppingCartAddItemAPIView.as_view(), name='shopping-cart-add-api'),
    path('shopping-cart-remove/', ShoppingCartRemoveItemAPIView.as_view(), name='shopping-cart-remove-api'),
    path('shopping-cart-add-quantity/', ShoppingCartAddQuantityItemAPIView.as_view(), name='shopping-cart-add-quantity-api'),
    path('shopping-cart-remove-quantity/', ShoppingCartRemoveQuantityItemAPIView.as_view(), name='shopping-cart-remove-quantity-api'),
    path('shopping-cart-clear/', ShoppingCartClearAPIView.as_view(), name='shopping-cart-clear')
]