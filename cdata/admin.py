from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Company, Supplier, CompanySupplierSpend, EDADesignFlow, SemiconductorFPGAPlatform  # new
from .models import Country, City, CompanyOffice, Contact
from import_export.admin import ImportExportModelAdmin


# Register your models here
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticker_symbol', 'revenue', 'estimated_eda_spend', 'industry')
    list_filter = ('industry', 'revenue', 'estimated_eda_spend')
    search_fields = ('name', 'ticker_symbol', 'industry')
    ordering = ('name',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')
    search_fields = ('name', 'abbreviation')
    ordering = ('name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name')
    ordering = ('name',)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'ticker_symbol')
    ordering = ('name',)


class CompanySupplierSpendAdmin(admin.ModelAdmin):
    list_display = ('company', 'supplier', 'spend')
    list_filter = ('supplier',)
    search_fields = ('company__name', 'supplier__name')
    ordering = ('company',)

class EDADesignFlowAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

class SemiconductorFPGAPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

class CompanyOfficeAdmin(admin.ModelAdmin):
    list_display = ('company', 'street_address', 'city', 'state_province', 'postal_code', 'country')
    search_fields = ('company__name', 'city__name', 'state_province', 'postal_code', 'country__name')
    ordering = ('company',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'job_title', 'email', 'company', 'company_office')
    list_filter = ('company__name', 'first_name', 'company_office__city__name')
    search_fields = ('last_name', 'first_name', 'email', 'company__name', 'company_office__city__name')
    ordering = ('company', 'last_name',)




admin.site.register(Company, CompanyAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Supplier, SupplierAdmin)   
admin.site.register(CompanySupplierSpend, CompanySupplierSpendAdmin)
admin.site.register(EDADesignFlow, EDADesignFlowAdmin)
admin.site.register(SemiconductorFPGAPlatform, SemiconductorFPGAPlatformAdmin)
admin.site.register(CompanyOffice, CompanyOfficeAdmin)
admin.site.register(Contact, ContactAdmin)
