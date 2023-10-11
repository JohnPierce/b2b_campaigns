from django.db import models
from django.apps import apps
from django.core.exceptions import ValidationError
from django.utils import timezone
from treebeard.mp_tree import MP_Node

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ticker_symbol = models.CharField(max_length=10, blank=True, null=True)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    revenue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    employees = models.IntegerField(blank=True, null=True)
    estimated_eda_spend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    sub_industry = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company_overview = models.TextField(blank=True, null=True)
    company_website = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.estimated_eda_spend is not None and self.revenue is not None:
            if self.estimated_eda_spend > self.revenue:
                raise ValidationError('Estimated EDA spend cannot be greater than revenue')

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    geonameid = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.country}'


class CompanyOffice(models.Model):
    id = models.AutoField(primary_key=True)
    company =  models.ForeignKey(Company, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    street_address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.company} {self.city}'

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    ticker_symbol = models.CharField(max_length=10, blank=True, null=True)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    revenue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    employees = models.IntegerField(blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    sub_industry = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    company_overview = models.TextField(blank=True, null=True)
    company_website = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class CompanySupplierSpend(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    spend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('company', 'supplier', 'year')

class EDADesignFlow(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class EDADesignFlowSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Spectre III')
    eda_design_flow = models.ForeignKey(EDADesignFlow, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.eda_design_flow.name} -> {self.name}'


class EDASupplierTools(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    eda_design_flow = models.ForeignKey(EDADesignFlow, on_delete=models.SET_NULL, blank=True, null=True)
    eda_design_flow_sub_category = models.ForeignKey(EDADesignFlowSubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    product_website = models.URLField(max_length=200, blank=True, null=True)
    meta_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    competitive_positioning = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.supplier.name}'
    
class EDASupplierTool(MP_Node):
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    eda_design_flow = models.ForeignKey(EDADesignFlow, on_delete=models.SET_NULL, blank=True, null=True)
    eda_design_flow_sub_category = models.ForeignKey(EDADesignFlowSubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    product_website = models.URLField(max_length=200, blank=True, null=True)
    meta_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    competitive_positioning = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class SemiconductorFPGAPlatform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100, default='Jane')
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, default='Doe')
    email = models.EmailField(max_length=100, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    office_phone = models.CharField(max_length=20, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    company_office = models.ForeignKey(CompanyOffice, on_delete=models.PROTECT, blank=True, null=True)
    company_group = models.ForeignKey('CompanyGroup', on_delete=models.SET_NULL, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CompanyGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    function = models.CharField(max_length=100, blank=True, null=True)
    group_headquarters = models.ForeignKey(CompanyOffice, on_delete=models.PROTECT, blank=True, null=True)  
    product_url_ref = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def clean(self):
        CompanyGroupHierarchy = apps.get_model('hierarchy', 'CompanyGroupHierarchy')
    
        if self.company is None:
            raise ValidationError('Company cannot be null')
    
        try:
            hierarchy_instance = self.companygrouphierarchy
        except CompanyGroupHierarchy.DoesNotExist:
            hierarchy_instance = None
    
        if not hierarchy_instance:
            return
    
        # Add name to the query for checking duplicates
        exists = CompanyGroupHierarchy.objects.filter(
            company_group__name=self.name, 
            parent=hierarchy_instance.parent
        ).exclude(pk=hierarchy_instance.pk).exists()
    
        if exists:
            raise ValidationError({
                'name': 'A group with this name and parent already exists.'
            })

    def __str__(self):
        return f'{self.company.name} -> {self.name}'
