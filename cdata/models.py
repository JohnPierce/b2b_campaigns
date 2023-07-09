from django.db import models
from django.apps import apps
from django.core.exceptions import ValidationError
from django.utils import timezone

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
        return self.name


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
    name = models.CharField(max_length=100)
    eda_design_flow = models.ForeignKey(EDADesignFlow, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class EDASupplierTools(models.Model):
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    eda_design_flow = models.ForeignKey(EDADesignFlow, on_delete=models.SET_NULL, blank=True, null=True)
    eda_design_flow_sub_category = models.ForeignKey(EDADesignFlowSubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    product_website = models.URLField(max_length=200)
    meta_data = models.TextField()
    description = models.TextField()
    competitive_positioning = models.TextField()
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
    email = models.EmailField(max_length=100)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    office_phone = models.CharField(max_length=20, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    company_office = models.ForeignKey(CompanyOffice, on_delete=models.PROTECT, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CompanyGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    function = models.CharField(max_length=100, blank=True, null=True)
    #hierarchy = models.ForeignKey(Hierarchy, on_delete=models.SET_NULL, blank=True, null=True)
    eda_design_flows = models.ManyToManyField(EDADesignFlow, blank=True)
    eda_tools_primary = models.ManyToManyField(EDASupplierTools, blank=True, related_name='eda_tools_primary')
    eda_tools_secondary = models.ManyToManyField(EDASupplierTools, blank=True, related_name='eda_tools_secondary')
    eda_tools_tertiary = models.ManyToManyField(EDASupplierTools, blank=True, related_name='eda_tools_tertiary')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hierarchy.get_full_name() if self.hierarchy else self.name
