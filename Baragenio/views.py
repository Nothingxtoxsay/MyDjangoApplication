

from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class HomePageView(TemplateView):
    template_name = 'app/about.html'