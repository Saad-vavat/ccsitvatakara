
from django.shortcuts import render


# Create your views here.
def alumni(request):
    

    context={}
    return render(request, 'alumnireg.html',context)

def home(request):
    return render(request, 'home.html')

