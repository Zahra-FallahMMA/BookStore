from . import views
from django.urls import path, include

app_name = 'shop'

urlpatterns = [
   path('', views.index, name='index'),
   path('store/', views.store, name='store'),
   path('product/', views.product, name='product'),
   path('checkout/', views.checkout, name='checkout'),
]