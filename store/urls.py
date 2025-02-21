from django.urls import path

from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
   
# )

urlpatterns = [path("", views.getRouting, name="routing"),
               path("products/", views.getProducts, name="products"),
               path("product/<str:pid>/",  views.getSingleProduct, name="single"),
               path("category/", views.getCategory, name="category" ),
            #    path('users/login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
            # #    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
            # path('users/profiles/', views.registerUser, name='register'),
               ]
