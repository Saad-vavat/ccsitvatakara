
from django.db import models



# Create your models here.




class Event(models.Model):
    event_image = models.ImageField(upload_to='events' , blank=True)
    event_date = models.DateField()
    event_name = models.CharField(max_length=30)
    event_desc = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering=['-event_date', '-event_name', ]

    def __str__(self) -> str:
        return self.event_name

class HomeGallery(models.Model):
    home_gall = models.ImageField(upload_to = 'home_gallery')
    def __str__(self) -> str:
        return str(self.home_gall)

class Notice(models.Model):
    notice = models.TextField()

    def __str__(self) -> str:
        return self.notice

    class Meta:
        ordering = ['-notice']

class Alert(models.Model):
    alert_desc= models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.alert_desc

class Slider(models.Model):
    image = models.ImageField(upload_to='slider')
    def __str__(self) -> str:
        return str(self.image)

class SpecialDay(models.Model):
    image = models.ImageField(upload_to="special day")
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=40, blank=True)
    def __str__(self) -> str:
        return self.title

class BatchinQp(models.Model):
    cat_id = models.AutoField(primary_key=True)
    batch = models.CharField(max_length=35)
    

    def __str__(self) :
        return self.batch 

class Qp(models.Model):
    qp = models.FileField(upload_to = 'Question Papers')
    year_of_qp = models.CharField(max_length=130)
    sub_name = models.CharField(max_length=100)
    Category = models.ForeignKey(BatchinQp, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.sub_name + ' ' + self.year_of_qp

class Testimonial(models.Model):
    subject = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'testimonial', blank =True)
    batch = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return self.name +' ' + self.subject[0:30]

class Exam_date_sheet(models.Model):
    batch = models.CharField(max_length=120)
    exam_date = models.DateField()
    exam_sheet_pdf = models.FileField(upload_to="exam_sheet")

    def __str__(self) -> str:
        return self.batch + ' ' + str(self.exam_date)
    











