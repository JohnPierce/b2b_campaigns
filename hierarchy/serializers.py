# serializers.py in your app directory

from rest_framework import serializers
from .models import CompanyGroupHierarchy, EmployeeHierarchy


class CompanyGroupHierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGroupHierarchy
        fields = ['id', 'company', 'company_group',
                  'parent', 'confidence', 'total_confidence', 'created_at']

class EmployeeHierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeHierarchy
        fields = ['id', 'company', 'employee', 'parent',
                  'confidence', 'total_confidence', 'created_at']
