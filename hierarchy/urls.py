# hierarchy/urls.py

from django.urls import path
from hierarchy.views import org_chart, org_chart_company

urlpatterns = [
    path('org_chart/', org_chart, name='org_chart'),
    path('org_chart_company/<int:company_id>/', org_chart_company, name='org_chart_company')
    # ... other url patterns
]
