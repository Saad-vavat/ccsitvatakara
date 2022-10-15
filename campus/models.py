
from django.db import models

# Create your models here.
class video_or_image(models.Model):
    image = models.ImageField(upload_to = 'campus_image', null=True, blank=True)
    video = models.FileField(upload_to='campus_video', null=True, blank=True)

    def __str__(self):
        return str(self.video) + str(self.image)