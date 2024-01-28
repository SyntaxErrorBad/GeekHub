from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.contrib.auth import authenticate, login, logout

from manageproducts.models import Product
from manageproducts.tasks import scrape_sears

from .serializers.productsserializer import ProductSerializer
from .serializers.productsserializer import ProductsCaregoriesSerializer
from .serializers.productsserializer import ProductAddProductsSerializer
from .serializers.loginserializer import LoginSerializer
from .serializers.shoppingcartserializer import ShoppingCartSerializer
from .serializers.shoppingcartserializer import ShoppingCartRemoveSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsCategoriesListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsCaregoriesSerializer


class ProductInfoListAPIView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(product_id = product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status = status.HTTP_404_NOT_FOUND)


class ProductAddProductAPIView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = ProductAddProductsSerializer(data = request.data)
        if serializer.is_valid():
            products = serializer.validated_data['product_ids']
            scrape_sears.delay(products)
            messages = "All Good"
        else:
            messages = "Something Wrong"

        return Response({'message': messages})


class LoginUserAPIView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username = username, password = password)
            if user and user.is_active:
                login(request, user)
                content = {
                        'user': str(request.user),
                        'login': 'successfully'
                    }
            else:
                content = {
                    'message': 'Wrong user or something'
                }

        return Response(content)


class LogoutUserAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({"message": "You quit from account"})

    def post(self, request):
        logout(request)
        return Response({"message": "You quit from account"})


class ShoppingCartAddItemAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ShoppingCartSerializer(data = request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            shopping_cart = request.session.get('shopping_cart') or []
            in_cart = False
            for item_in_cart in shopping_cart:
                if item_in_cart["ID"] == product_id:
                    in_cart = True
                    break
            if in_cart is False:
                shopping_cart.append({
                    "ID": product_id,
                    "Count": quantity
                })
            request.session['shopping_cart'] = shopping_cart
            if in_cart is False:
                return Response({"message": f"Product with ID: {product_id} "
                                            f"and quantity {quantity} was successfully added"})
            else:
                return Response({"message": f"Product with ID: {product_id} was in cart"})


class ShoppingCartRemoveItemAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ShoppingCartRemoveSerializer(data = request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            shopping_cart = request.session.get('shopping_cart') or []
            in_cart = False
            for item_in_cart in shopping_cart:
                if item_in_cart["ID"] == product_id:
                    in_cart = True
                    shopping_cart.remove(item_in_cart)
            request.session['shopping_cart'] = shopping_cart
            if in_cart:
                return Response({"message": f"Product with ID: {product_id} was successfully delet"})
            else:
                return Response({"message": f"Product with ID: {product_id}. Not in the Cart"})


class ShoppingCartAddQuantityItemAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ShoppingCartSerializer(data = request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            shopping_cart = request.session.get('shopping_cart') or []
            in_cart = False
            for item_in_cart in shopping_cart:
                if item_in_cart['ID'] == product_id:
                    in_cart = True
                    item_in_cart['Count'] += quantity
            request.session['shopping_cart'] = shopping_cart
            if in_cart:
                return Response(
                    {"message": f"Product with ID: {product_id}. Quantity {quantity} was successfully added"})
            else:
                return Response({"message": f"Product with ID: {product_id}. Not in the Cart"})


class ShoppingCartRemoveQuantityItemAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ShoppingCartSerializer(data = request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            shopping_cart = request.session.get('shopping_cart') or []
            in_cart = False
            for item_in_cart in shopping_cart:
                if item_in_cart['ID'] == product_id:
                    in_cart = True
                    item_in_cart['Count'] -= quantity
            request.session['shopping_cart'] = shopping_cart
            if in_cart:
                return Response({"message": f"Product with ID: {product_id}. "
                                            f"Quantity {quantity} was successfully delet"})
            else:
                return Response({"message": f"Product with ID: {product_id}. Not in the Cart"})


class ShoppingCartClearAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.session['shopping_cart'] = []
        return Response({"message": "The cart was cleaned!"})

    def post(self, request):
        request.session['shopping_cart'] = []
        return Response({"message": "The cart was cleaned!"})
