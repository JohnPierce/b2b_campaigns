 

from django.db import models
from django.apps import apps
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils import timezone

from cdata.models import Company, CompanyGroup, Contact
from cdata.models import EDASupplierTools
from cdata.models import Supplier

from hierarchy.models import CompanyGroupHierarchy
from hierarchy.choices import CONFIDENCE_CHOICES


class CompanyGroupEDASupplierTools(models.Model):
    """Model representing a company group's EDA supplier tools."""

    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(
        EDASupplierTools, on_delete=models.PROTECT)
    company_group = models.ForeignKey(
        CompanyGroup, on_delete=models.PROTECT)
    confidence = models.DecimalField(
        max_digits=2, decimal_places=1, choices=CONFIDENCE_CHOICES, default=0.5)
    description = models.TextField(blank=True, null=True)
    primary = models.BooleanField(default=False)
    secondary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.company.name} {self.company_group.name} {self.name}'
