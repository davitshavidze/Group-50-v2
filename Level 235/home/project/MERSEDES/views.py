from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MERSEDES

# Create your views here.
def home_page(req):
  cars = MERSEDES.objects.all().values()
  context = {
    "mersedes": cars
  }
  template = loader.get_template('mersedes_home.html')
  return HttpResponse(template.render(context, req))

def details(req, id):
  car = MERSEDES.objects.get(id = id)
  template = loader.get_template('details.html')
  context = {
    "details": car
  }

  return HttpResponse(template.render(context, req))