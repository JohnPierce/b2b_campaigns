from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CompanyGroupEDADesignFlow
from .models import CompanyGroupEDASupplierTools
from cdata.models import Company
from hierarchy.models import CompanyGroupHierarchy
from import_export.admin import ImportExportModelAdmin




# Register your models here
class CompanyGroupEDADesignFlowAdmin(admin.ModelAdmin):
    list_display = ('get_comp_name', 'company_group', 'name')
    list_filter = ('company_group', 'name')
    search_fields = ('company_group', 'name')
    ordering = ('company_group','name')

    def get_comp_name(self, obj):
        return obj.company.name

class CompanyGroupEDASupplierToolsAdmin(admin.ModelAdmin):
    list_display = ('get_comp_name', 'company_group', 'name')
    list_filter = ('company_group', 'name')
    search_fields = ('company_group', 'name')
    ordering = ('company_group','name')

    def get_comp_name(self, obj):
        return obj.company.name






admin.site.register(CompanyGroupEDADesignFlow, CompanyGroupEDADesignFlowAdmin)
admin.site.register(CompanyGroupEDASupplierTools, CompanyGroupEDASupplierToolsAdmin)

