from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room,Topic,User,Message
from .serializers import RoomSerializer,TopicSerializer,UserSerializer,MessageSerializer


@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/forums',
        'GET /api/forums/:id',
        'GET /api/topics',
        'GET /api/topics/:id',
        'GET /api/users',
        'GET /api/users/:id',
        'GET /api/messages',
        'GET /api/messages/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    serializer=RoomSerializer(rooms,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    rooms=Room.objects.get(id=pk)
    serializer=RoomSerializer(rooms,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getTopics(request):
    topics=Topic.objects.all()
    serializer=TopicSerializer(topics,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTopic(request,pk):
    topics=Topic.objects.get(id=pk)
    serializer=TopicSerializer(topics,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request,pk):
    users=User.objects.get(id=pk)
    serializer=UserSerializer(users,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getMessages(request):
    users=Message.objects.all()
    serializer=MessageSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessage(request,pk):
    users=Message.objects.get(id=pk)
    serializer=MessageSerializer(users,many=False)
    return Response(serializer.data)