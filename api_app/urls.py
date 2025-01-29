from django.urls import path
from . import views

urlpatterns = [
    path('', views.Json_details_View, name='api-response'),
]