#converts python object into json data
from rest_framework.serializers import ModelSerializer
from base.models import Room,Topic,User,Message

class RoomSerializer(ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class TopicSerializer(ModelSerializer):
    class Meta:
        model=Topic
        fields='__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        exclude=['password','is_superuser','last_login','is_staff','is_active','user_permissions']
    
class MessageSerializer(ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'