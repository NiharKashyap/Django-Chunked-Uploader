
from django.core.files import File
from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import random
from .models import FileModel
import time
from django.conf import settings
import os

# Create your views here.

def index(request):
    return render(request,"index.html")

@csrf_exempt
def upload_partial(request):
    if request.method=="GET":
        return JsonResponse({'Message':"Success"})
    elif request.method=="POST":
        tukura = request.FILES["source"]
        if request.POST["file_id"]=="None":
            obj = FileModel.objects.create(file=tukura, is_chunk=True, chunk_number=request.POST["chunk"])
        else:
            obj = FileModel.objects.create(file_id=request.POST["file_id"], file=tukura, is_chunk=True, chunk_number=request.POST["chunk"])
        return JsonResponse({'Message':"Success", "file_id":obj.file_id})

@csrf_exempt
def upload_complete(request):
    id = request.POST["file_id"]
    objects = FileModel.objects.all().filter(file_id=id, is_chunk=True)
    file_path = os.path.join(settings.MEDIA_ROOT, 'files\\' , request.POST["file_name"])
    with open(file_path, 'wb') as outfile:
        for fname in objects:
            with open(fname.file.path, 'rb') as infile:
                for line in infile:
                    outfile.write(line)
    
    img_path = 'files/' + request.POST["file_name"]
    try:
        instance = FileModel(file_id=id, is_chunk=False)
        instance.file = img_path
        instance.save()
    except Exception as e:
        print(e)
    objects.delete()
    
    return JsonResponse({"Message":instance.id, "url":instance.file.url})
        

def show_file(request, id):
    obj = FileModel.objects.get(id=id)
    print(obj.file.url)
    print(obj.file.path)
    return JsonResponse({'file':obj.file.url})
    