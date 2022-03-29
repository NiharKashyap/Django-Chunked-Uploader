import uuid
from django.core.files import File
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FileModel
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
        model_file = File(tukura)
        file_path = os.path.join(settings.MEDIA_ROOT, 'files\\' , request.POST["file_id"] + "_" + request.POST["chunk"])
        f = open(file_path, "wb")
        f.write(model_file.read())
        f.close()
        return JsonResponse({'Message':"Success"})

@csrf_exempt
def upload_complete(request):
    id = request.POST["file_id"]
    name = request.POST["file_name"]
    
    rootdir = os.path.join(settings.MEDIA_ROOT, 'files\\')
    file_arr =[]
    for _, _, files in os.walk(rootdir):
        for file in files:
            if file.startswith(id):
                file_arr.append(file)
    
    with open(rootdir + '\\' + name, 'wb') as outfile:
        for fname in file_arr:
            with open(rootdir + '\\' + fname, 'rb') as infile:
                for line in infile:
                    outfile.write(line)
                infile.close()
                os.remove(rootdir + '\\' + fname)
    
    img_path = 'files/' + name
    
    try:
        instance = FileModel(file_id=id, is_chunk=False)
        instance.file = img_path
        instance.save()
    except Exception as e:
        print(e)

    return JsonResponse({"Message":instance.id, "url":instance.file.url})
        

def show_file(request, id):
    obj = FileModel.objects.get(id=id)
    print(obj.file.url)
    print(obj.file.path)
    return JsonResponse({'file':obj.file.url})
    