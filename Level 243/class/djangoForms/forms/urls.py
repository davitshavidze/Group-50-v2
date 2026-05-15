from django.urls import path
from .views import form_test

urlpatterns = [
    path('', form_test, name='forms')
]
