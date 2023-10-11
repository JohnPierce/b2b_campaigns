from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone

from cdata.models import Company, CompanyGroup, Contact
from cdata.models import EDASupplierTools
from cdata.models import Supplier

from hierarchy.models import CompanyGroupHierarchy
from hierarchy.choices import CONFIDENCE_CHOICES

from .models import CompanyGroupEDASupplierTools


class CompanyGroupEDASupplierToolsTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company')
        self.company_group = CompanyGroup.objects.create(
            name='Test Company Group', company=self.company)
        self.eda_supplier_tool = EDASupplierTools.objects.create(
            name='Test EDA Supplier Tool')
        self.company_group_eda_supplier_tool = CompanyGroupEDASupplierTools.objects.create(
            name=self.eda_supplier_tool, company_group=self.company_group)

    def test_str_method(self):
        expected_str = f'{self.company.name} {self.company_group.name} {self.eda_supplier_tool.name}'
        self.assertEqual(str(self.company_group_eda_supplier_tool), expected_str)

    def test_confidence_choices(self):
        invalid_confidence = 2.0
        with self.assertRaises(ValidationError):
            self.company_group_eda_supplier_tool.confidence = invalid_confidence
            self.company_group_eda_supplier_tool.full_clean()

    def test_created_at(self):
        now = timezone.now()
        self.assertLess(self.company_group_eda_supplier_tool.created_at, now)from django.test import TestCase

# Create your tests here.
