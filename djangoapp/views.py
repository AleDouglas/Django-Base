from django.shortcuts import render

# Views importadas 
from django.views.generic import TemplateView 


# Nossa página inicial
class homeView(TemplateView):
    template_name = 'home.html'