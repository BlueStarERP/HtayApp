"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from myapp.views import *
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'CartViewSet', CartViewSet, basename='CartViewSet')


# The API URLs are now determined automatically by the router.




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the router URLs
    path('api/pro/', ProductListView.as_view(), name='product-list'),
    path('api/pro/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('base/', base_view, name='base'),
    path('SetupItemView/', SetupItemView.as_view(), name='SetupItemView'),
    path('', POSView.as_view(), name='POSView'),
    path('SaveOrderView/', SaveOrderView.as_view(), name='SaveOrderView'),
    path('CartItemDetailView/<int:pk>/', CartItemDetailView.as_view(), name='CartItemDetailView'),
    path('ProductDetailView/<int:pk>/', ProductDetailView.as_view(), name='ProductDetailView'),
    path('SaleReportView/', SaleReportView.as_view(), name='SaleReportView'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)