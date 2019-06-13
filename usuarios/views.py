from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import UsuarioSerializer
from .models import Usuario

# Create your views here.
class UsuarioListView(ListAPIView):
    serializer_class = UsuarioSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        keyword = self.kwargs['keyword']
        return Usuario.objects.filter(Q(name__icontains=keyword) | Q(username__icontains=keyword)).order_by('-priority').order_by('name')