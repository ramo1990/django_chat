from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('checkview/', views.checkview, name='checkview'),
    path('getMessages/<str:room>/', views.getMessages, name = 'getMessages'),
    path('<str:room>/', views.room, name="room"),
]
