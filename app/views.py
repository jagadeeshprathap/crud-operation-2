from django.shortcuts import render

# Create your views here.
from app.models import *

def display_Dept(request):
    lod=Dept.objects.all()
    d={'dept':lod}

    return render(request,'display_Dept.html',d)

def display_Emp(request):
    loe=Emp.objects.all()
    d={'emp':loe}

    return render(request,'display_Emp.html',d)