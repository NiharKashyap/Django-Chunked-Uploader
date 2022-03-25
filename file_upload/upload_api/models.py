from django.db import models
import uuid
# Create your models here.

class FileModel(models.Model):
    file_id = models.UUIDField(default=uuid.uuid4)
    file = models.FileField(upload_to='files/')
    is_chunk = models.BooleanField()
    chunk_number = models.BigIntegerField()