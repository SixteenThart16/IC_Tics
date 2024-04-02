from rest_framework import serializers
from .models import Motos

class MotosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Motos
        fields= '__all__' 
        