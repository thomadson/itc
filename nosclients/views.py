from django.shortcuts import render

# Create your views here.
def nosclients(request):
    return render(request,'nosclients.html')
