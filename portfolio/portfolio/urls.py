from django.contrib import admin
from django.urls import path
from app_home import views
urlpatterns = [
    #rota, view, nome ref
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
]
