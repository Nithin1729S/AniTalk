from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

rooms=[
    {'id':1,'name':'Lets Learn Python'},
    {'id':2,'name':'Design with me'},
    {'id':3,'name':'Frontend Dev'},
]

def home(request):
    #return HttpResponse("Home Page")
    context={'rooms':rooms}
    return render(request,'home.html',context)

def room(request,pk):
    #return HttpResponse("Room")
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i
    context={'room':room}

    return render(request,'room.html',context)
