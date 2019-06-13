from django.urls import path
from usuarios import views

urlpatterns = [
    path('usuarios/<str:keyword>/', views.UsuarioListView.as_view(), name='list-usuarios')
]