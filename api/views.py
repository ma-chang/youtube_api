from rest_framework import viewsets
from rest_framework import generics
from .serializers import UserSerializer, VideoSerializer
from rest_framework.permissions import AllowAny
from .models import Video

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    serializers_class = UserSerializer
    permissions_classes = (AllowAny,)


class VideoViewSet(generics.ModelViewSet):
    queryset = Video.objects.all()
    serializers_class = VideoSerializer
