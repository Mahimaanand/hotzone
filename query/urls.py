from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inquiry/', views.inquiry, name ="inquiry"),
    path('add_data_to_db/', views.add_data_to_db, name ="add_data_to_db"),
]