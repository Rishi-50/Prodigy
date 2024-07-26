from django.urls import path
from base_app import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path('health/', views.health_check, name='health_check'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
]