
from django.shortcuts import render
from .models import Course

# Create your views here.
def course(request):
    context={
        'course': Course.objects.all(),
    }
    return render(request, 'courseslist.html', context)
