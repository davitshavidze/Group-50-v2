from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.models import products

# Create your views here.
def catalog(req):
  prods = products.objects.all().values()
  context = {
    "prods":prods 
  }
  template = loader.get_template('catalog.html')
  return HttpResponse(template.render(context, req))

def details(req, id):
  prod = products.objects.get(id = id)
  template = loader.get_template('details.html')
  context = {
    "details": prod
  }
  return HttpResponse(template.render(context, req))