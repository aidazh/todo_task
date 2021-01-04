from django.urls import path
from .views import index, update_task, delete_task

urlpatterns = [
    path('', index, name='home-list'),
    path('update/<str:pk>/', update_task, name='update_task'),
    path('delete/<str:pk>/', delete_task, name='delete'),
]