from django.shortcuts import render, get_object_or_404

from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from .models import Sector, Industry, VerticalMarket, Application, Algorithm  # new
from rest_framework import viewsets
from .serializers import SectorSerializer, IndustrySerializer, VerticalMarketSerializer, ApplicationSerializer, AlgorithmSerializer  # new

# Create your views here.

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all().order_by('name')
    serializer_class = SectorSerializer

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all().order_by('name')
    serializer_class = IndustrySerializer

class VerticalMarketViewSet(viewsets.ModelViewSet):
    queryset = VerticalMarket.objects.all().order_by('name')
    serializer_class = VerticalMarketSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('name')
    serializer_class = ApplicationSerializer

class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.all().order_by('name')
    serializer_class = AlgorithmSerializer