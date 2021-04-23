from django.shortcuts import render,redirect
from .models import destination,f,fd,adrs
from django.contrib.auth.models import User,auth
from django.contrib import messages
import os,json,string,random

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
    client_ip = request.META['REMOTE_ADDR']
    print("the ip is: "+client_ip)
    S = 10  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    # print the random data  
    if request.method == 'POST':
        print("kaat")
        p = request.POST['directories']
        dic = json.loads(p)
        dic2 = {}
        if dic[next(iter(dic))].count('/') == 1:
            fname = dic[next(iter(dic))].split('/')[0]
        
        p2 = 'C:/Users/ADARSH/pro/aadi/media/fm/' + fname

        #creating the databases of the given ip addresses
        adrs.objects.create(ipinfo=client_ip)

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
        return render(request, 'uploaded.html',{'rand': ran}) 
    else:
        #add = request.GET["adrs"]
        #print(add)
        '''x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip)'''
        
        return render(request, 'upload.html',{'rand': ran})
    
def bhome(request):
    return redirect("home")
