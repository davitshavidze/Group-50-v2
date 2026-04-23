from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import activity

# Create your views here.

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def details(request, id):
  activities = activity.objects.get(id = id)
  template = loader.get_template('details.html')
  context = {
    'details': activities
  }
  return HttpResponse(template.render(context, request))