from django.urls import path

from api.views import products_list, product_id, categories_list, category_id, products_by_category

urlpatterns = [
    path('products/', products_list),
    path('products/<int:id>', product_id),
    path('categories/', categories_list),
    path('categories/<int:category_id>/', category_id),
    path('categories/<int:category_id>/products/', products_by_category)
]