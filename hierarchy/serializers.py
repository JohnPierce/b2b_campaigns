# serializers.py in your app directory

from rest_framework import serializers
from .models import CompanyGroupHierarchy, EmployeeHierarchy
from cdata.models import Contact, CompanyGroup, Company


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

class ContactHierarchySerializer(serializers.ModelSerializer):
    parent_id = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'email', 'job_title', 'company_group', 'company_office', 'parent_id']

    def get_parent_id(self, obj):

        company_group = obj.company_group

        if company_group:
            parent_group_hierarchy = CompanyGroupHierarchy.objects.filter(group=company_group).first()
            if parent_group_hierarchy:
                parent_group = parent_group_hierarchy.parent
                return parent_group.id if parent_group else None
        
        return None