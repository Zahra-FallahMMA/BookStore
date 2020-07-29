from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
   path('', views.index, name='index'),
   path('product/<int:pk>/', views.product, name='product'),
   path('checkout/', views.checkout, name='checkout'),
   path('login/', auth_views.LoginView.as_view(), name='login'),
   path('to-bank/<int:order_id>/', views.to_bank, name='to_bank'),
   path('callback/', views.callback, name='callback'),
]