from django.db import models
from cdata.models import Company, CompanyGroup, Contact
from .choices import CONFIDENCE_CHOICES

# Create your models here.

class CompanyGroupHierarchy(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    company_group = models.OneToOneField(CompanyGroup, on_delete=models.PROTECT)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    confidence = models.DecimalField(max_digits=2, decimal_places=1, choices=CONFIDENCE_CHOICES, default=0.5)
    total_confidence = models.DecimalField(max_digits=3, decimal_places=2, default=0.5, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.parent is not None:
            self.total_confidence = self.confidence * self.parent.total_confidence
        else:
            self.total_confidence = self.confidence
        super(CompanyGroupHierarchy, self).save(*args, **kwargs)

    def get_full_name(self):
        if self.parent:
            return f'{self.parent.get_full_name()} -> {self.company_group.name}'
        else:
            return f'{self.company.name} -> {self.company_group.name}'

    def __str__(self):
        return self.get_full_name()

class EmployeeHierarchy(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    employee = models.OneToOneField(Contact, on_delete=models.PROTECT)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    confidence = models.DecimalField(max_digits=2, decimal_places=1, choices=CONFIDENCE_CHOICES, default=0.5)
    total_confidence = models.DecimalField(max_digits=3, decimal_places=2, default=0.5, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.parent is not None:
            self.total_confidence = self.confidence * self.parent.total_confidence
        else:
            self.total_confidence = self.confidence
        super(EmployeeHierarchy, self).save(*args, **kwargs)

    def get_full_hierarchy(self):
        if self.parent:
            return f'{self.parent.get_full_hierarchy()} -> {self.employee.first_name} {self.employee.last_name}'
        else:
            return f'{self.employee.first_name} {self.employee.last_name}'

    def __str__(self):
        return self.get_full_hierarchy()