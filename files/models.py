from django.db import models
from django.conf import settings

# Create your models here.

class FileStatus(models.TextChoices):
    uploaded = 'uploaded'
    compressed = 'compressed'

class UploadedFile(models.Model):
    file = models.FileField(upload_to=settings.UPLOADS_FOLDER + "/", max_length=255)
    name = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=FileStatus,default=FileStatus.uploaded)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.status}) uploaded: {self.uploaded_at:%d-%b-%Y %H:%M:%S}'
