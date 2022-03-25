from django.contrib import admin
from .models import FileModel
# Register your models here.

@admin.register(FileModel)
class FileAdmin(admin.ModelAdmin):
    list_display = ['file_id', 'chunk_number']