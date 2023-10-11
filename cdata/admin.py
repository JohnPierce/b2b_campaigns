from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms
from .models import Company, Supplier, CompanySupplierSpend, EDADesignFlow, SemiconductorFPGAPlatform  # new
from .models import Country, City, CompanyOffice, Contact, EDADesignFlowSubCategory, EDASupplierTools, EDASupplierTool, CompanyGroup
from import_export.admin import ImportExportModelAdmin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from follow.models import SocialMedia, FollowUp
from hierarchy.models import CompanyGroupHierarchy
from design_flow.models import CompanyGroupEDASupplierTools
from design_flow.models import EDASupplierTools
from design_flow.admin import CompanyGroupEDASupplierToolsForm




class CompanyGroupHierarchyInline(admin.TabularInline):
    model = CompanyGroupHierarchy
    extra = 1

class CompanyGroupInline(admin.TabularInline):
    model = CompanyGroup
    extra = 1

class CompanyGroupEDASupplierToolsInline(admin.TabularInline):
    model = CompanyGroupEDASupplierTools
    form = CompanyGroupEDASupplierToolsForm
    extra = 1


class CompanyGroupEDADesignFlowSubCategoryInline(admin.TabularInline):  
    model = EDADesignFlowSubCategory
    extra = 1

#class CompanyGroupEDASupplierToolsInline(admin.TabularInline):
#    model = CompanyGroupEDASupplierTools
#   extra = 1

#class EDASupplierToolsInline(admin.TabularInline):
#    model = EDASupplierTools
#    extra = 1


# Register your models here
class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyGroupInline]
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
#    inlines = [EDASupplierToolsInline]
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


    
class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1

class FollowUpInline(admin.TabularInline):
    model = FollowUp
    extra = 1



class ContactAdmin(admin.ModelAdmin):
    inlines = [SocialMediaInline, FollowUpInline]
    change_form_template = 'admin/cdata/contacts/change_form.html'
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

class EDASupplierToolAdmin(TreeAdmin):
    form = movenodeform_factory(EDASupplierTool)
    list_display = ('name', 'supplier', 'eda_design_flow', 'eda_design_flow_sub_category', 'product_website', 'competitive_positioning')
    list_filter = ('eda_design_flow__name', 'eda_design_flow_sub_category__name')
    search_fields = ('name', 'eda_design_flow__name', 'eda_design_flow_sub_category__name')
    ordering = ('name', 'supplier', 'eda_design_flow__name',)

class CompanyGroupAdmin(admin.ModelAdmin):
    # Need to add the model intto design flow CompanyGroupEDADesignFlowSubCategory... 
    inlines = [CompanyGroupHierarchyInline, CompanyGroupEDASupplierToolsInline]
    #inlines = [CompanyGroupHierarchyInline]
    change_form_template = 'admin/cdata/companygroup/change_form.html'
    list_display = ('get_compgroup_name', 'function', 'product_url_ref')
    search_fields = ('name', 'function', 'product_url_ref')
    list_filter = ('company',)
    ordering = ('company', 'name')

    def get_compgroup_name(self, obj):
        return f'{obj.company.name} -> {obj.name}'
    
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)




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
admin.site.register(EDASupplierTool, EDASupplierToolAdmin)

