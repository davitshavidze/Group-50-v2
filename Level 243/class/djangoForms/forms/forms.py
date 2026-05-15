from django import forms
from .models import newModel

class main_form(forms.ModelForm):
  class Meta:
    model = newModel
    fields = '__all__'

    style = {
      'style': "border: none; color: red; background-color: blue;"
    }

    widgets = {
      'name': forms.TextInput(attrs={
        'placeholder': "Name...",
        'class': 'name',
        'style': style['style']
      }),
    
      'surname': forms.TextInput(attrs={
        'placeholder': "Surname...",
        'class': 'surname',
        'style': style['style']
      }),

      'age': forms.TextInput(attrs={
        'placeholder': "Age...",
        'class': 'age',
        'style': style['style']
      }),

      'email': forms.EmailInput(attrs={
        'placeholder': "Email...",
        'class': 'email',
        'style': style['style']
      }),

      'password': forms.PasswordInput(attrs={
        'placeholder': "Password...",
        'class': "pass",
        'style': style['style']
      })
    }