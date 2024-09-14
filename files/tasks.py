import os
import zipfile
from celery import shared_task
from .models import UploadedFile
from django.conf import settings

@shared_task
def compress_files():
    files_to_compress = UploadedFile.objects.filter(status='uploaded')

    for file_record in files_to_compress:
        file_real_name_parts = file_record.file.name.split('/')
        file_real_name = file_real_name_parts[-1]
        
        file_path = os.path.join(settings.BASE_DIR, settings.UPLOADS_FOLDER, file_real_name)
        compressed_file_path = os.path.join(settings.BASE_DIR, settings.UPLOADS_FOLDER, f"{file_real_name}.zip")       

         # Create a zip file for the uncompressed file
        with zipfile.ZipFile(compressed_file_path, 'w') as zipf:
            zipf.write(file_path, os.path.basename(file_path))

        # Replace original file with the compressed file in the database
        file_record.name = f"{file_real_name}.zip"
        file_real_name_parts[-1] = f"{file_real_name}.zip"
        file_record.file.name = '/'.join(file_real_name_parts)
        file_record.status = 'compressed'
        
        file_record.save()

        # Delete the original file
        os.remove(file_path)
