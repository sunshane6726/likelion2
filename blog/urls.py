from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('<int:pk>/', views.detail, name = 'detail'),
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('newblog/',views.blogpost, name= 'nowblog'),
    path('update/<int:pk>/', views.update, name = 'update'),
    path('delete/<int:pk>/', views.delete, name = 'delete'),
    path('index/', views.index, name = 'index'),

    
] 
