from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from BMW.models import BMWS

# Create your views here.
def home_page(req):
  cars = BMWS.objects.all().values()
  context = {
    "bmws": cars
  }
  template = loader.get_template('bmw_home.html')
  return HttpResponse(template.render(context, req))

def details(req, id):
  car = BMWS.objects.get(id = id)
  template = loader.get_template('details.html')
  context = {
    "details": car
  }

  return HttpResponse(template.render(context, req))