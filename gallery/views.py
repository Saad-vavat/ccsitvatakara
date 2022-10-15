
from django.shortcuts import render

from .models import Category, Gallery



# Create your views here.
def gallery(request):
    cat = Category.objects.all()
    context={'cat': cat}
    return render(request, 'gallery.html', context)

def ReadCat(request, id):
    cats = Category.objects.get(cat_id = id)
    gallery = Gallery.objects.filter(category = cats)
    context={'cat': cats, 'gallery':gallery}
    return render(request, 'gallerycategory.html', context)

