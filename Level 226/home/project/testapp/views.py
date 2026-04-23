from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import first_model
from .models import second_model
from .models import assistants

# Create your views here.
def home_page(request):

  students = first_model.objects.all().values()
  mentors = second_model.objects.all().values()
  assistants_arr = assistants.objects.all().values()
  context = {
    "students": students,
    "mentors": mentors,
    "assistants": assistants_arr
  }

  template = loader.get_template('home.html')
  return HttpResponse(template.render(context, request))

def about_page(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def services_page(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())

def contact_page(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())