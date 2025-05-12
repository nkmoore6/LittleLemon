from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('Menu/', views.Menu, name='Menu'),
    path('Menu/', views.MenuItemsView.as_view()),
    path('Menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
