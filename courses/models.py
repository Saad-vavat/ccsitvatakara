
from django.db import models

# Create your models here.
class Course(models.Model):
    course_image = models.ImageField(upload_to = 'course')
    course_name = models.CharField(max_length=100)
    course_brief = models.CharField(max_length=200,blank=True)
    cours_desc = models.TextField()

    def __str__(self) -> str:
        return self.course_name