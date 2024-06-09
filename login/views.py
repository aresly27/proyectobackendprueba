from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import AllowAny
from usuario.models import Usuario
from .models import Login
from .serializers import LoginSerializer

# Create your views here.

class LoginView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        correo = request.data.get('correo')
        password = request.data.get('password')
        user = authenticate(username=correo, password=password)
        print(correo)
        print(password)
        print(user)
        if user is not None:
            usuario_obj = Usuario.objects.get(correo=correo)
            print(usuario_obj)
            Login.objects.create(usuario=usuario_obj)
            return Response({'mensaje': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'mensaje': 'Usuario o contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
