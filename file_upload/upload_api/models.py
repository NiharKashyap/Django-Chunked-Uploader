from django.db import models
import os
from django.dispatch import receiver

class FileModel(models.Model):
    file_id = models.CharField(max_length=20)
    file = models.FileField(upload_to='files/')
    is_chunk = models.BooleanField()
    chunk_number = models.BigIntegerField(default=0)

@receiver(models.signals.post_delete, sender=FileModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)