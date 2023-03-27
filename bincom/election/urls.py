from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('total', views.total, name = 'total'), 
    path('new_result', views.new_result, name = 'new_result'),                
]
