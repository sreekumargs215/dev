from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.messages import constants as messages
from django.shortcuts import render,redirect
from datetime import timedelta, datetime
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def portfolio(request):
    context={}
    return render(request,"index.html",context)