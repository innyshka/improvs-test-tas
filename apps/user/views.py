from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from apps.user.serializers import RegisterUserSerializer, LoginUserSerializer
from apps.user.utils.func import custom_to_representation


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = AllowAny,


class LoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = AllowAny,

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.validated_data
        user = User.objects.filter(username=request_data.get("username")).first()
        if user and user.check_password(request_data.get("password")):
            return Response(custom_to_representation(user))
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)