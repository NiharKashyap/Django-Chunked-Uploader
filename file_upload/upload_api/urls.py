from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('upload_partial/', upload_partial),
    path('upload_complete/', upload_complete)
]
