from django.shortcuts import render
from .models import Personnels

# Create your views here.
def personnels(request):
    personnels=Personnels.objects.all()
    return render(request,'personnels.html',{'personnels':personnels})
