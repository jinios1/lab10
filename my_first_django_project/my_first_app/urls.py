from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world_no_param'),
    
    path('hello/<str:name>/', views.hello_world, name='hello_world'),

    path('redirect-example/', views.redirect_example, name='redirect_example'),

    path('json-example/', views.json_example, name='json_example'),

    path('show-cookies/', views.show_cookies, name='show_cookies'),
]
