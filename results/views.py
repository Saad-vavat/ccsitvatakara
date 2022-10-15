from django.shortcuts import render

# Create your views here.
def result(request):
    return render(request, 'results1.html')