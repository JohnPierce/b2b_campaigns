from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Company, Supplier, CompanySupplierSpend, EDADesignFlow, SemiconductorFPGAPlatform  # new
from .models import Country, City, CompanyOffice, Contact, EDADesignFlowSubCategory, EDASupplierTools, CompanyGroup
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
    list_filter = ('company',)
    ordering = ('company',)

class CompanyGroupAdmin(admin.ModelAdmin):
    list_display = ('get_compgroup_name', 'function', 'product_url_ref')
    search_fields = ('name', 'function', 'product_url_ref')
    list_filter = ('company',)
    ordering = ('company', 'name')

    def get_compgroup_name(self, obj):
        return f'{obj.company.name} -> {obj.name}'

class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'job_title', 'email', 'company', 'company_office', 'company_group')
    list_filter = ('company__name', 'first_name', 'company_office__city__name')
    search_fields = ('last_name', 'first_name', 'email', 'company__name', 'company_office__city__name')
    ordering = ('company', 'last_name',)

class EDADesignFlowSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'eda_design_flow', 'description')
    list_filter = ('eda_design_flow__name',)
    search_fields = ('name', 'eda_design_flow__name', 'description')
    ordering = ('eda_design_flow', 'name',)

class EDASupplierToolsAdmin(admin.ModelAdmin):
    list_display = ('get_supplier_name', 'get_eda_design_flow_name', 'name', 'product_website', 'competitive_positioning')
    list_filter = ('eda_design_flow__name', 'eda_design_flow_sub_category__name')
    search_fields = ('name', 'eda_design_flow__name', 'eda_design_flow_sub_category__name')
    ordering = ('eda_design_flow__name', 'supplier', 'name',)

    def get_supplier_name(self, obj):
        return obj.supplier.name
    def get_eda_design_flow_name(self, obj):
        return obj.eda_design_flow.name






admin.site.register(Company, CompanyAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Supplier, SupplierAdmin)   
admin.site.register(CompanySupplierSpend, CompanySupplierSpendAdmin)
admin.site.register(EDADesignFlow, EDADesignFlowAdmin)
admin.site.register(SemiconductorFPGAPlatform, SemiconductorFPGAPlatformAdmin)
admin.site.register(CompanyOffice, CompanyOfficeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(EDADesignFlowSubCategory, EDADesignFlowSubCategoryAdmin)
admin.site.register(EDASupplierTools, EDASupplierToolsAdmin)
admin.site.register(CompanyGroup, CompanyGroupAdmin)

