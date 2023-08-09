from django.db import models
from django.apps import apps
from django.core.exceptions import ValidationError
from django.utils import timezone
from cdata.models import Company, CompanyGroup, Contact, EDADesignFlow, EDASupplierTools
from hierarchy.models import CompanyGroupHierarchy
from hierarchy.choices import CONFIDENCE_CHOICES


# Create your models here.

class CompanyGroupEDADesignFlow(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(EDADesignFlow, on_delete=models.PROTECT) 
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    company_group = models.ForeignKey(CompanyGroup, on_delete=models.PROTECT) 
    company_group_hier = models.ForeignKey(CompanyGroupHierarchy, on_delete=models.PROTECT)
    confidence = models.DecimalField(max_digits=2, decimal_places=1, choices=CONFIDENCE_CHOICES, default=0.5)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.company.name} {self.company_group.name} {self.name}'
    
class CompanyGroupEDASupplierTools(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(EDASupplierTools, on_delete=models.PROTECT) 
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    company_group = models.ForeignKey(CompanyGroup, on_delete=models.PROTECT) 
    company_group_hier = models.ForeignKey(CompanyGroupHierarchy, on_delete=models.PROTECT)
    confidence = models.DecimalField(max_digits=2, decimal_places=1, choices=CONFIDENCE_CHOICES, default=0.5)
    description = models.TextField(blank=True, null=True)
    primary = models.BooleanField(default=False)
    secondary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.company.name} {self.company_group.name} {self.name}'