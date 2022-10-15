from django.shortcuts import render
from .models import video_or_image

# Create your views here.
  
def campuslife(request):
    context={
        'videoimage' : video_or_image.objects.all()
        }
    
    
    return render(request, 'aboutcampuslife.html',context)


