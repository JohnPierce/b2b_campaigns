from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ticker_symbol = models.CharField(max_length=10, blank=True, null=True)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    revenue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
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

class Supplier(models.Model):
    name = models.CharField(max_length=100)

class CompanySupplierSpend(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
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

class SemiconductorFPGAPlatform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
