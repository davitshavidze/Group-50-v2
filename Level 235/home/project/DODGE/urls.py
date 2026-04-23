from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('details/<int:id>/', views.details, name='details')
]
