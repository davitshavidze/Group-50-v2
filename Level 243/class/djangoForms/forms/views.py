from django.shortcuts import render
from .forms import main_form

# Create your views here.
def form_test(request):
  context = {
    "form": main_form()
  }

  if request.method == "POST":
    form = main_form(request.POST)

    if form.is_valid():
      form.save()

  return render(request, 'index.html', context)