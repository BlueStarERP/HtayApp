from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.contrib.auth import authenticate, login, logout
import json
import datetime

from .models import *
from .serializers import *
from .forms import *

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status



# Create your views here.
#API

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None  # Disable pagination for this viewset
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = None  # Disable pagination for this viewset
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None  # Disable pagination for this viewset
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        search = request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        
        paginator = Paginator(queryset, 10)  # Show 10 products per page
        page_number = request.query_params.get('page', 1)
        try:
            products = paginator.page(page_number)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


####################################################### Template 
def base_view(request):
    return render(request, 'base.html')


class SetupItemView(View):
    def get(self, request):
        itemlist = Product.objects.all()
        categorylist = Category.objects.all()
        context = {'itemlist':itemlist, 'categorylist':categorylist}
        return render(request, 'setup_item.html', context)
        
class POSView(View):
    def get(self, request):
        itemlist = Product.objects.all()
        today_cart = Cart.objects.filter(date=datetime.date.today())
        categorylist = Category.objects.all()
        context = {'itemlist':itemlist, 'categorylist':categorylist, 'today_cart':today_cart}
        return render(request, 'pos.html', context)
    
class SaveOrderView(View):
    def post(self, request):
        json_data = request.body
        data = json.loads(json_data)
        # print(type(data))
        # print(data)
        cart = Cart.objects.create(total=0)  # Create a new cart instance
        for item in data:
            product_id = int(item['id'])
            quantity = int(item['quantity'])
            price = int(item['price'])
            print(f"Product ID: {product_id}, Quantity: {quantity}, Price: {price}")
            product = Product.objects.get(id=product_id)
            cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity, price=price)
            cart.total += cart_item.price * cart_item.quantity
        
        cart.save()  # Save the cart with the updated total
        

        return JsonResponse({'message': 'Order saved successfully!'})
        
class CartItemDetailView(View):
    def get(self, request, pk):
        try:
            cart = Cart.objects.get(id=pk)
            cart_items = CartItem.objects.filter(cart=cart)
            return render(request, 'invoice_detail.html', {'cart': cart, 'cart_items': cart_items})
            # serializer = CartItemSerializer(cart_items, many=True)
            # return JsonResponse(serializer.data, safe=False)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart not found'}, status=404)