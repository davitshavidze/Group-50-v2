from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from testapp.models import todo


# Create your views here.

def home(req):
  todos = todo.objects.all().values()
  context = {
    "todos": todos
  }

  template = loader.get_template('index.html')
  return HttpResponse(template.render(context, req))