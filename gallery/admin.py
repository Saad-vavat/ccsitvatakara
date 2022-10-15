from multiprocessing import Event
from django.contrib import admin


from .models import Category,Gallery
# Register your models here.
admin.site.register(Category),
admin.site.register(Gallery)

class EventPhotosInline(admin.StackedInline):
    model = Gallery

class EventAdmin(admin.ModelAdmin):
    inlines = [EventPhotosInline,]
