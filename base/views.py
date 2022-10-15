

from django.shortcuts import render
from .models import * 
# Create your views here.
def home(request):
    context = {
        'event': Event.objects.all(),
        'gallery': HomeGallery.objects.all(),
        'notice': Notice.objects.all(),
         'alert': Alert.objects.all(),
        'slider':Slider.objects.all(),
        'special':SpecialDay.objects.all(),
        'testimonial':Testimonial.objects.all()
   }
    
    return render(request, 'index.html', context)



def qp_link(request):
    cat = BatchinQp.objects.all()
    context={'cat': cat}
    return render(request, 'previous_cat.html',context)

def qp(request, id):
    cats = BatchinQp.objects.get(cat_id = id)
    qp = Qp.objects.filter(Category = cats)
    context = {'cat': cats, 'qp':qp}
    return render(request, 'previousqp.html', context)

def exam(request):
    context={
        'exam': Exam_date_sheet.objects.all()
    }
    return render(request, 'exam.html', context)








