from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CompanyGroupEDADesignFlow
from .models import CompanyGroupEDASupplierTools
from import_export.admin import ImportExportModelAdmin



# Register your models here
class CompanyGroupEDADesignFlowAdmin(admin.ModelAdmin):
    list_display = ('company', 'company_group', 'name')
    list_filter = ('company', 'company_group', 'name')
    search_fields = ('company', 'company_group', 'name')
    ordering = ('company','company_group','name')

class CompanyGroupEDASupplierToolsAdmin(admin.ModelAdmin):
    list_display = ('company', 'company_group', 'name')
    list_filter = ('company', 'company_group', 'name')
    search_fields = ('company', 'company_group', 'name')
    ordering = ('company','company_group','name')






admin.site.register(CompanyGroupEDADesignFlow, CompanyGroupEDADesignFlowAdmin)
admin.site.register(CompanyGroupEDASupplierTools, CompanyGroupEDASupplierToolsAdmin)

