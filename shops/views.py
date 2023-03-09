from django.shortcuts import render
from .models import Shop

# Create your views here.

from django.shortcuts import render, HttpResponse

def home(request):

   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

   if x_forwarded_for:

       ip = x_forwarded_for.split(',')[0]

   else:

       ip = request.META.get('REMOTE_ADDR')

  

   return HttpResponse("Welcome! You are visiting from: {}".format(ip))


def index(request):
    shops = Shop.objects.all()
    context ={
        'shops': shops
        }
    return render(request, "index.html", context)

def nearby(request):
    shops = Shop.objects.all()
    context ={
        'shops': shops
        }
    return render(request, "index.html", context)
