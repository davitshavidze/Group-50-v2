from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import DODGES

# Create your views here.
def home_page(req):
  cars = DODGES.objects.all().values()
  context = {
    "dodges": cars
  }
  template = loader.get_template('dodge_home.html')
  return HttpResponse(template.render(context, req))

def details(req, id):
  car = DODGES.objects.get(id = id)
  template = loader.get_template('details.html')
  context = {
    "details": car
  }

  return HttpResponse(template.render(context, req))