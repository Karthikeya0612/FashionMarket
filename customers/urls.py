from django.urls import path
from . import views

urlpatterns = [
    path('customers/login/', views.login, name='login'),
    path('customers/signup/', views.signup, name='signup'),
    path('customers/signup/signup',views.signup, name='signup'),
    path('customers/login/login',views.login, name='login'),
    path('customers/logout',views.logout, name='logout'),
    path('customers/cart',views.cart, name='cart'),
]
