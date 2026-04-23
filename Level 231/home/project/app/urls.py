from django.urls import path
from . import views

urlpatterns = [
  path('', views.catalog, name='catalog'),
  path('details/<int:id>', views.details, name='details')
]
