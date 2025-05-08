from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('Menu/', views.Menu, name='Menu'),
    path('api/', include(router.urls)),
]
