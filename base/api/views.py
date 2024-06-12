from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
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
def getForums(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getForum(request, pk):
    try:
        room = Room.objects.get(id=pk)
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "Forum not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTopic(request, pk):
    try:
        topic = Topic.objects.get(id=pk)
        serializer = TopicSerializer(topic, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "Topic not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessage(request, pk):
    try:
        message = Message.objects.get(id=pk)
        serializer = MessageSerializer(message, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)