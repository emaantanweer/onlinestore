from django.shortcuts import render
from .serializer import ProductSerializer, CategorySerializer
from.models import Product, Category
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings



BASE_URL = settings.REACT_BASE_URL


@api_view(['GET'])
def getRouting(request):
    routes =[
        "/api/products/",
        "/api/products/insert/",
        "/api/products/update/",

        "/api/products/top/",
        "/api/products/<id>/",
        "/api/products/delete/<id>/",
        "/api/products/update/<id>/"
    ]
    return Response(routes)

@api_view(['GET'])
def getCategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getSingleProduct(request, pid):
    product = Product.objects.get(id=pid)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['name'] = user.name
#         # ...

#         return token


