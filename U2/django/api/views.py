from rest_framework import viewsets
from .serializer import MotosSerializer
from .serializer import Motos

class MotosViewSet(viewsets.ModelViewSet):
    queryset=Motos.objects.all()
    serializer_class=MotosSerializer
