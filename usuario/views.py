from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Usuario
from .serializers import UsuarioSerializer

# Create your views here.
class CreateUsuario(APIView):
    def delete(self, request, usuario_id):
        usuario_obj = get_object_or_404(Usuario, pk=usuario_id)
        usuario_obj.status=False
        usuario_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
