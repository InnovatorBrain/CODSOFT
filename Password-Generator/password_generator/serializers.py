from rest_framework import serializers
from .models import *

class GenPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model: GenPassword
        fields = '__all__'
        