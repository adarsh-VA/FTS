from django.shortcuts import render,redirect
from .models import destination,f,userinfo
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
    #cookies printing
    cook = request.COOKIES.get('unique-id') 
    #unq = json.loads(cook)
    #print(unq)

    #print(type(unq))
    print("error occured")
    S = 10  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data. 

    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    if not cook:
        userinfo.objects.create(uniqueid=ran)
    
    if request.method == 'POST':
        print("kaat")
        p = request.POST['directories']
        recid = request.POST['rec-id']
        dic = json.loads(p)
        dic2 = {}
        if dic[next(iter(dic))].count('/') == 1:
            fname = dic[next(iter(dic))].split('/')[0]

        #creating the databases of the given ip addresses
        
        for x in request.FILES.getlist("files"):
            st = dic[x.name]
            dic2[x.name] = st[:-len(x.name)]
            
        print(cook)
        db = userinfo.objects.get(uniqueid=cook)
        db.foldername=fname
        db.filedic=dic2
        db.save()
        db2 = userinfo.objects.filter(uniqueid=recid).exists()
        if db2:
            db3 = userinfo.objects.get(uniqueid=recid)
            db3.recdic = dic2
            db3.save()
            #fd.objects.create(foldername=fname,filedic=dic2)
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
        db4 = userinfo.objects.get(uniqueid=cook)
        recdata = db4.recdic
        #recdata.replace('\"', '\\"')
        print(json.dumps(recdata))
        return render(request, 'upload.html',{'rand': ran,'recdata':recdata})
    
def bhome(request):
    return redirect("home")
