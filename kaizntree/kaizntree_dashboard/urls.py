from django.urls import path, include
from .views import (
    ItemListView,
    AddItemView,
    AddCategoryView,
    SearchListView
)

urlpatterns = [
    path('api/', ItemListView.as_view()),
    path('items/', AddItemView.as_view(), name='item-list'),
    path('categories/', AddCategoryView.as_view(), name='add-category'),
    path('search/', SearchListView.as_view(), name='search-items')
]