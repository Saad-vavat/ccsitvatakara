

from django.db import models



class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    poster = models.ImageField(upload_to ="poster")

    class Meta:
        ordering = ['-poster', '-name']

    def __str__(self) :
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to = 'gallery', null=True )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

        
    def __str__(self) :
        return str(self.image) +' ' +str(self.category)