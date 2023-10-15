from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('beauty/', views.beauty, name='beauty'),
    path('boys/', views.boys, name='boys'),
    path('girls/', views.girls, name='girls'),
    path('grooming/', views.grooming, name='grooming'),
    path('infants/', views.infants, name='infants'),
    path('kurtis/', views.kurtis, name='kurtis'),
    path('maternity/', views.maternity, name='maternity'),
    path('sandals/', views.sandals, name='sandals'),
    path('sarees/', views.sarees, name='sarees'),
    path('shirts/', views.shirts, name='shirts'),
    path('shoes/', views.shoes, name='shoes'),
    path('toys/', views.toys, name='toys'),
    path('trousers/', views.trousers, name='trousers'),
]