
from django.db import models

# Create your models here.
class placement(models.Model):
    image = models.ImageField(upload_to= 'placement', blank=True)
    name = models.CharField(max_length=200)
    batch = models.IntegerField()
    placed_at = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to= 'placement' ,blank = True)
   

    def __str__(self) :
        return  self.name + ' ' + str(self.batch)

class Placement_year(models.Model):
     current_placement_year = models.CharField(max_length=10, blank=True)

     def __str__(self) -> str:
         return self.current_placement_year