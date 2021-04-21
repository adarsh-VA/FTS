from django.shortcuts import render,redirect
from .models import destination,f,fd,adrs
from django.contrib.auth.models import User,auth
from django.contrib import messages
import os,json

'''def upload(request):
    if request.method == 'POST':
        fs = request.FILES['doc']
        up = f(ff = fs)
        up.save()
        print(fs)
        return redirect('upload') 
    else:
        return render(request, 'upload.html')'''
    

def upload(request):
    if request.method == 'POST':
        print("kaat")
        p = request.POST['directories']
        dic = json.loads(p)
        dic2 = {}
        if dic[next(iter(dic))].count('/') == 1:
            fname = dic[next(iter(dic))].split('/')[0]
        
        p2 = 'C:/Users/ADARSH/pro/aadi/media/fm/' + fname

        if not os.path.exists(p2):  
            for x in request.FILES.getlist("files"):
                st = dic[x.name]
                path = 'C:/Users/ADARSH/pro/aadi/media/fm/' + st[:-len(x.name)]
                dic2[x.name] = path
                if not os.path.exists(path):
                    os.makedirs(path)
                def process(f):
                    with open(path + str(x), 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk) 
                process(x)
            fd.objects.create(foldername=fname,filedic=dic2)
        return render(request, 'uploaded.html') 
    else:
        #add = request.GET["adrs"]
        #print(add)
        return render(request, 'upload.html')
    
def bhome(request):
    return redirect("home")
