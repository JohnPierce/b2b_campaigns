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
                  'company', 'company_office', 'job_title']

class ContactBriefSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ['full_name', 'job_title']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    

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

class CompanyGroupContactSerializer(serializers.ModelSerializer):
    contact_set = ContactBriefSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyGroup
        fields = '__all__'

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        company_group = CompanyGroup.objects.create(**validated_data)
        for contact_data in contacts_data:
            Contact.objects.create(company_group=company_group, **contact_data)
        return company_group

class CompanyOfficeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)
    country_name = serializers.CharField(source='country.name', read_only=True) 
    class Meta:
        model = CompanyOffice
        fields = ['id', 'company_name', 'street_address', 'street_address2',
                  'city_name', 'state_province', 'postal_code',
                  'country_name', 'created_at']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'abbreviation', 'latitude', 'longitude']

class EDASupplierToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EDASupplierTools
        fields = ['name', 'supplier', 'eda_design_flow', 'eda_design_flow_sub_category',
                  'product_website', 'meta_data', 'description', 'competitive_positioning', 'created_at']

