import random
import string
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Password
from .serializers import PasswordSerializer


class PasswordGenerateViewSet(viewsets.ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer

    def create(self, request, *args, **kwargs):
        length = request.data.get("length")

        try:
            length = int(length)  # Convert the string to an integer.
        except ValueError:
            return Response(
                {"length": "Invalid value. Please provide an integer."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if length <= 0:
            return Response(
                {"length": "Length must be a positive number."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = "".join(random.choice(characters) for _ in range(length))

        password = Password.objects.create(length=length, value=generated_password)
        serializer = PasswordSerializer(password)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
