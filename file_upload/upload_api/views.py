from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import random
from .models import FileModel

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
        
        # folder='my_folder/' 
        # fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
        # filename = fs.save("File " + str(request.POST["chunk"]), tukura)
        # file_url = fs.url(filename)
        return JsonResponse({'Message':"Success", "file_id":obj.file_id})

@csrf_exempt
def upload_complete(request):
    id = request.POST["file_id"]
    objects = FileModel.objects.all().filter(file_id=id)
    
    print(len(objects))
    print(objects[0].file_id)
    return JsonResponse({"Message":"Success"})
        