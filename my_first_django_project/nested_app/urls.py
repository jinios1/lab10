from django.urls import path
from . import views

urlpatterns = [
    path('', views.nested_home, name='nested_home'),
    path('about/', views.nested_about, name='nested_about'),
    path('contacts/', views.nested_contacts, name='nested_contacts'),
]
