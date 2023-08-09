# serializers.py in your app directory

from rest_framework import serializers
from .models import Contact, Company, CompanyGroup, EDADesignFlow, EDASupplierTools

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'middle_name', 'last_name',
                  'email','mobile_phone', 'office_phone', 'info',
                  'created_at',
                  'company', 'company_office', 'job_title',
                  'linkedin_url', 'twitter_url', 'company_url_ref']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'ticker_symbol', 'market_cap',
                  'revenue', 'employees', 'estimated_eda_spend',
                  'sector', 'industry', 'sub_industry',
                  'created_at', 'company_overview',
                  'company_website']
