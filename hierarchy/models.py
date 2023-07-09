from django.db import models
from cdata.models import Company, CompanyGroup, Contact

# Create your models here.

class CompanyGroupHierarchy(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    company_group = models.OneToOneField(CompanyGroup, on_delete=models.PROTECT)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        if self.parent:
            return f'{self.parent.get_full_name()} -> {self.company_group.name}'
        else:
            return self.company_group.name

    def __str__(self):
        return self.get_full_name()

class EmployeeHierarchy(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    employee = models.OneToOneField(Contact, on_delete=models.PROTECT)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_hierarchy(self):
        if self.parent:
            return f'{self.parent.get_full_hierarchy()} -> {self.employee.first_name} {self.employee.last_name}'
        else:
            return f'{self.employee.first_name} {self.employee.last_name}'

    def __str__(self):
        return self.get_full_hierarchy()