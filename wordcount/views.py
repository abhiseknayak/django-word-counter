from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    text=request.GET['text']
    l=text.split(' ')
    dict={}
    for i in range(0,len(l)):
        if(l[i] not in dict):
            dict[l[i]]=1
        else:
            dict[l[i]]+=1

    dict2=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    print(dict2)
    return render(request,'count.html',{'fulltext':text,'words':len(l),'diction':dict2})

def about(request):
    return render(request,'about.html')
