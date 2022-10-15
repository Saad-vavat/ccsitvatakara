
from django.shortcuts import render
from .models import *
# Create your views here.
def Placement(request):

    context = {
        'placement':placement.objects.all(),
        'placement_year': Placement_year.objects.all
    }

    return render(request, 'placement.html', context)