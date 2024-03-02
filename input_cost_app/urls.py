from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_cost, name='input_cost'),
]
