from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms
from .models import CompanyGroupEDASupplierTools





# Register your models here


class CompanyGroupEDASupplierToolsForm(forms.ModelForm):
    """Form for CompanyGroupEDASupplierTools model."""

    class Meta:
        model = CompanyGroupEDASupplierTools
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].queryset = self.fields["name"].queryset.order_by("name")



class CompanyGroupEDASupplierToolsAdmin(admin.ModelAdmin):
    """Admin class for CompanyGroupEDASupplierTools model."""
    
    form = CompanyGroupEDASupplierToolsForm
    list_display = ('name', 'get_comp_name', 'get_supplier_name', 'company_group')
    list_filter = ('name', 'company_group',)
    search_fields = ('name', 'company_group',)
    ordering = ('name', 'company_group',)

    def get_comp_name(self, obj):
        """Get company name."""
        return obj.company_group.company.name
    
    def get_supplier_name(self, obj):
        """Get supplier name."""
        return obj.name.supplier.name

admin.site.register(CompanyGroupEDASupplierTools, CompanyGroupEDASupplierToolsAdmin)



