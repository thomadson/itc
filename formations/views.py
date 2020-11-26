from django.shortcuts import render
from .models import Formations

# Create your views here.
def formations(request):
    formations=Formations.objects.all()
    return render(request,'formations.html',{'formations':formations})