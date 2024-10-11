from django.urls import include, path
from rest_framework import routers
from login import views

app_name = 'prueba'
routers = routers.DefaultRouter()

# routers.register('usuario', permisos.UserPermiso, 'usuario')

urlpatterns = [
    path('', include(routers.urls)),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
