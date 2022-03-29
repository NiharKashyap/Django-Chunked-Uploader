from django.urls import path
# from .views_save_db import *
from .views_save_file import *


urlpatterns = [
    path('', index),
    path('upload_partial/', upload_partial),
    path('upload_complete/', upload_complete),
    path('show_file/<int:id>', show_file)
]
