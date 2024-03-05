from django.urls import path
from .views import cost_analysis

urlpatterns = [
    path('graph/', cost_analysis, name='cost_analysis'),
]
