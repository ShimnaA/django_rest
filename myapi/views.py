from rest_framework import viewsets

from .serializers import ActorSerializer
from .models import Actor

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by('name')
    serializer_class = ActorSerializer