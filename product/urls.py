from django.urls import path
from .views import (product_list, product_detail,landing_page)

app_name='product'

urlpatterns=[
    path('landing/',landing_page, name='landing' ),
    path('',product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('detail/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]