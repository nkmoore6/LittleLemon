from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking, MenuItem
from .serializer import MenuSerializer, BookingSerializer, MenuItemSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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
        permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]    
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
# api
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permission_class = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_class.append(IsAdminUser)
        return [permission() for permission in permission_class]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permission_class = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]