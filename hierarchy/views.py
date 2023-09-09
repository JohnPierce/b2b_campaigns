from django.shortcuts import render, get_object_or_404, redirect
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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CompanyGroupHierarchy, EmployeeHierarchy
from rest_framework import viewsets
from .serializers import CompanyGroupHierarchySerializer, EmployeeHierarchySerializer






# Create your views here.


def company_group_hierarchy_list(request):
    company_hierarchy = CompanyGroupHierarchy.objects.all()  # Get all Company objects from the database
    return render(request, 'hierarchy/company_hierarchy_list.html', {'company_hierarchy': company_hierarchy})


class CompanyGroupHierarchyViewSet(viewsets.ModelViewSet):
    queryset = CompanyGroupHierarchy.objects.all().order_by('company')
    serializer_class = CompanyGroupHierarchySerializer

class EmployeeHierarchyViewSet(viewsets.ModelViewSet):
    queryset = EmployeeHierarchy.objects.all().order_by('employee')
    serializer_class = EmployeeHierarchySerializer

@api_view(['GET'])
def org_chart(request):
    if request.method == 'GET':
        root_nodes = CompanyGroupHierarchy.objects.filter(parent__isnull=True)
        chart_data = [build_hierarchy(node) for node in root_nodes]

        return Response(chart_data)

@api_view(['GET'])
def org_chart_company(request, company_id):
    if request.method == 'GET':
        root_nodes = CompanyGroupHierarchy.objects.filter(parent__isnull=True, company=company_id)
        chart_data = [build_hierarchy(node) for node in root_nodes]

        return Response(chart_data)
    
def build_hierarchy(node):
    children = []
    for child in node.companygrouphierarchy_set.all():
        children.append(build_hierarchy(child))
    
    contacts = [{"name": f"{contact.first_name} {contact.last_name}", "type": "contact"} for contact in node.company_group.contact_set.all()]

    return {
        "name": node.company_group.name,
        "type": "group",
        "children": children + contacts
    }
    
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
