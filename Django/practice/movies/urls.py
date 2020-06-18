from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
]
