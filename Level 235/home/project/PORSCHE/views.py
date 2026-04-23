from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home_page(req):
  template = loader.get_template('porsche_home.html')
  return HttpResponse(template.render())