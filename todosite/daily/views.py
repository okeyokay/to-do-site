import datetime
from .models import Task

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def today(request):
    last_24_hours = timezone.now() - datetime.timedelta(hours=24)
    tasks = Task.objects.filter(pub_date__gte=last_24_hours)
    context = {"latest_tasks": tasks}
    # return render(request, "daily/today.html", context)
    return HttpResponse("This page will be filled with a HTML template soon.")
