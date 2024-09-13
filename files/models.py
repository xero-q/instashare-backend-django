from django.db import models
from django.conf import settings

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to=settings.UPLOADS_FOLDER+'/',max_length=255)
    original_name = models.CharField(max_length=255)
    new_name = models.CharField(max_length=255, blank=True, null=True)
    size = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default='uploaded') 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_name if self.new_name else self.original_name
