from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Menu
from .serializer import MenuSerializer
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def about(request):
    return render(request, 'about.html')

class Groupviewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
def get_permissions(self):
    permission_classes = [IsAuthenticated]
    if self.request.method != 'GET':
        permission_classes = [IsAuthenticated]
    return [permission() for permission in permission_classes]    
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer