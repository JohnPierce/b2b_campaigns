from django.contrib import admin
from .models import CompanyGroupHierarchy
from .models import EmployeeHierarchy
from import_export.admin import ImportExportModelAdmin


# Register your models here
class CompanyGroupHierarchyAdmin(admin.ModelAdmin):
    list_display = ('get_company_id', 'company', 'company_group', 'parent')
    list_filter = ('company', 'company_group', 'parent')
    search_fields = ('company', 'company_group', 'parent')
    ordering = ('company','company_group','parent')

    def get_company_id(self, obj):
        return obj.company.id
    get_company_id.short_description = 'Company ID'

class EmployeeHierarchyAdmin(admin.ModelAdmin):
    list_display = ('company', 'employee', 'parent')
    list_filter = ('company', 'employee', 'parent')
    search_fields = ('company', 'employee', 'parent')
    ordering = ('company','employee','parent')






admin.site.register(CompanyGroupHierarchy, CompanyGroupHierarchyAdmin)
admin.site.register(EmployeeHierarchy, EmployeeHierarchyAdmin)


