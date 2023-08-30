# serializers.py in your app directory

from rest_framework import serializers
from .models import Contact, Company, CompanyGroup, EDADesignFlow, EDASupplierTools, CompanyOffice
from .models import City, Country

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

class CompanyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGroup
        fields = ['id', 'name', 'company', 'function','group_headquarters',
                  'product_url_ref', 'description', 'created_at']

class CompanyOfficeLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyOffice
        fields = ['id', 'company', 'street_address', 'street_address2',
                  'city', 'state_province', 'postal_code',
                  'country', 'created_at']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'abbreviation', 'latitude', 'longitude']


