from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from hierarchy.models import CompanyGroupHierarchy, EmployeeHierarchy
from rest_framework import generics, viewsets

from .models import (Company, CompanyOffice, Contact, EDADesignFlow,
                     EDADesignFlowSubCategory, EDASupplierTools, CompanyGroup)
from .serializers import (CitySerializer, CompanyGroupContactSerializer,
                          CompanyGroupSerializer, CompanyOfficeSerializer,
                          CompanySerializer, ContactSerializer,
                          CountrySerializer, EDASupplierToolsSerializer)

import os
import sys
import time

import requests
import numpy as np
import pandas as pd





# Create your views here.


def company_list(request):
    companies = Company.objects.all()  # Get all Company objects from the database
    return render(request, 'cdata/company_list.html', {'companies': companies})

def get_groups_by_company(request, company_id):
    groups = CompanyGroup.objects.filter(company__id=company_id)
    data = [{"id": group.id, "name": group.name} for group in groups]
    return JsonResponse(data, safe=False)

def get_office_location_by_company(request, company_id):
    offices = CompanyOffice.objects.filter(company__id=company_id)
    data = [{"id": office.id, "name": f'{office.company} {office.city}'} for office in offices]
    return JsonResponse(data, safe=False)

def get_edadesignflowsubcategory_by_edadesignflow(request, edadesignflow_id):
    edadesignflowsubcategories = EDADesignFlowSubCategory.objects.filter(eda_design_flow__id=edadesignflow_id)
    data = [{"id": edadesignflowsubcategory.id, "name": f'{edadesignflowsubcategory.eda_design_flow.name} {edadesignflowsubcategory.name}'} for edadesignflowsubcategory in edadesignflowsubcategories]
    return JsonResponse(data, safe=False)

def get_edasuppliertools_by_edadesignflow(request, edadesignflow_id):
    edasuppliertools = EDASupplierTools.objects.filter(eda_design_flow__id=edadesignflow_id)
    data = [{"id": edasuppliertool.id, "name": edasuppliertool.name} for edasuppliertool in edasuppliertools]
    return JsonResponse(data, safe=False)

def get_edasuppliertools(request):
    # Retrieve query parameters
    eda_design_flow_id = request.GET.get('eda_design_flow_id', None)
    subcategory_id = request.GET.get('subcategory_id', None)
    vendor_id = request.GET.get('vendor_id', None)

    # Perform filtering based on query parameters
    queryset = EDASupplierTools.objects.all()
    if eda_design_flow_id:
        queryset = queryset.filter(eda_design_flow__id=eda_design_flow_id)
        
    if subcategory_id:
        queryset = queryset.filter(eda_design_flow_sub_category__id=subcategory_id)
    
    if vendor_id:
        queryset = queryset.filter(supplier__id=vendor_id)
    
    # Serialize the filtered data
    serializer = EDASupplierToolsSerializer(queryset, many=True)

    # Convert the serialized data to JSON
    data = serializer.data

    return JsonResponse(data, safe=False)

class HomePageView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'index.html'
    login_url = 'login'

    def get_queryset(self):
        return Company.objects.all()

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('first_name')
    serializer_class = ContactSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

class CompanyWithGroupHierarchyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        # Get distinct company ids with hierarchy
        company_ids = CompanyGroupHierarchy.objects.values_list('company', flat=True).distinct()

        return Company.objects.filter(id__in=company_ids)

class CompanyWithEmployeeHierarchyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        # Get distinct company ids with hierarchy
        company_ids = EmployeeHierarchy.objects.values_list('company', flat=True).distinct()

        return Company.objects.filter(id__in=company_ids)

class CompanyGroupViewSet(viewsets.ModelViewSet):
    queryset = CompanyGroup.objects.all().order_by('name')
    serializer_class = CompanyGroupContactSerializer

class CompanyGroupContactViewSet(viewsets.ModelViewSet):
    queryset = CompanyGroup.objects.all()
    serializer_class = CompanyGroupContactSerializer

class CompanyOfficeViewSet(viewsets.ModelViewSet):
    queryset = CompanyOffice.objects.all().order_by('company')
    serializer_class = CompanyOfficeSerializer

class CityWithCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CitySerializer

    def get_queryset(self):
        # Get distinct city ids with company
        city_ids = CompanyOffice.objects.values_list('city', flat=True).distinct()

        return City.objects.filter(id__in=city_ids)

class CountryWithCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountrySerializer

    def get_queryset(self):
        # Get distinct country ids with company
        country_ids = CompanyOffice.objects.values_list('country', flat=True).distinct()

        return Country.objects.filter(id__in=country_ids)
    
@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(info__icontains=search_term) |
            Q(phone__iexact=search_term)
        )
        context = {
            'search_term': search_term,
            'contacts': search_results.filter(manager=request.user)
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')