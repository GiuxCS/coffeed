from django.shortcuts import render
from django.views.generic import TemplateView

class SplashView(TemplateView):
    template_name = "index.html"





#from django.views.generic import TemplateView

#from django.http import HttpResponse
# Create your views here.

"""
def TestView(request, **kwargs):
    return HttpResponse("|-|3|_|_0 \/\/0R|_|>")
    """

#class SplashView(TemplateView):
    #template_name = "index.html"