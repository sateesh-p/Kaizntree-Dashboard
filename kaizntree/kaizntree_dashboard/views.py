# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from rest_framework import status
from .serializers import ItemSerializer, CategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
class AddItemView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if isinstance(request.data, list):  # Check if the request data is a list
            serializer = ItemSerializer(data=request.data, many=True)
        else:
            serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddCategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SearchListView(APIView):
    def get(self, request):
        # Get query parameters for search criteria
        sku_query = request.query_params.get('sku', '')
        name_query = request.query_params.get('name', '')
        category_query = request.query_params.get('category', '')
        tags_query = request.query_params.get('tags', '')
        stock_status_query = request.query_params.get('stock_status', '')

        # Filter items based on search criteria
        items = Item.objects.all()
        if sku_query:
            items = items.filter(sku__icontains=sku_query)
        if name_query:
            items = items.filter(name__icontains=name_query)
        if category_query:
            items = items.filter(category__icontains=category_query)
        if tags_query:
            items = items.filter(tags__name__icontains=tags_query)
        if stock_status_query:
            items = items.filter(stock_status__icontains=stock_status_query)

        # Serialize the queryset
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)