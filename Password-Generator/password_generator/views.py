import random
import string
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GenPassword
from .serializers import GenPasswordSerializer

class PasswordGenerator(APIView):
    def get(self, request, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        serializer = GenPasswordSerializer(data={'password': password})
        if serializer.is_valid():
            serializer.save()
            return Response({'password': password}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeneratedPasswordList(APIView):
    def get(self, request):
        passwords = GenPassword.objects.all()
        serializer = GenPasswordSerializer(passwords, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
