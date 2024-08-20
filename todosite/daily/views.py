from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def today(request):
    return HttpResponse("This is the daily tasks page.")
