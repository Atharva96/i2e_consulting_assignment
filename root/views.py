from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

def folderchecker():
    folderpath = os.path.join(os.getcwd(),'textfiles')
    if not os.path.exists(folderpath):os.makedirs(folderpath)
    return folderpath



def index(request):
    folderpath = folderchecker()

    if request.method=="POST":
        filename = request.POST['filename']
        content = request.POST['content']
        if not filename.endswith('.txt'): filename = filename+'.txt'
        filepath = os.path.join(folderpath,filename)
        if os.path.exists(filepath):os.remove(filepath)
        with open(filepath, 'w', encoding='utf-8') as newfile:
            newfile.write(str(content))

        FileStorage(filename=filename,content=content).save()
        

        print(content)
        files = list(FileStorage.objects.all().order_by('-id'))
        return render(request, 'root/index.html', {"files":files})
    else:
        files = list(FileStorage.objects.all().order_by('-id'))
        return render(request, 'root/index.html', {"files":files})
    

 
 


 


def deletefile(request,id):
    folderpath = os.path.join(os.getcwd(),'textfiles')
    file = FileStorage.objects.get(id=id)
    filepath = os.path.join(folderpath,file.filename)
    os.remove(filepath)
    file.delete()
    return redirect('index')




def updatefile(request,id):
    folderpath = folderchecker()
    if request.method=="POST":
        filename = request.POST['filename']
        content = request.POST['content']
        if not filename.endswith('.txt'): filename = filename+'.txt'
        filepath = os.path.join(folderpath,filename)
        if os.path.exists(filepath):os.remove(filepath)
        with open(filepath, 'w', encoding='utf-8') as newfile:
            newfile.write(str(content))

        file = FileStorage.objects.filter(id=id).first()
        if file is not None:
            file.delete()
            FileStorage(filename=filename,content=content).save()
        else:
            FileStorage(filename=filename,content=content).save()

        return redirect('index')
    else:        
        data = FileStorage.objects.filter(id=id).first()
        files = list(FileStorage.objects.all().order_by('-id'))

        return render(request, 'root/index.html', {"data":data,'files':files})

