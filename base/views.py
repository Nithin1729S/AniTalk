from django.shortcuts import render
from .models import Room
# Create your views here.
#from django.http import HttpResponse

# rooms=[
#     {'id':1,'name':'Lets Learn Python'},
#     {'id':2,'name':'Design with me'},
#     {'id':3,'name':'Frontend Dev'},
# ]

def home(request):
    rooms=Room.objects.all()  #query
    #return HttpResponse("Home Page")
    context={'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    #return HttpResponse("Room")
    room=Room.objects.get(id=pk)
    context={'room':room}

    return render(request,'base/room.html',context)
