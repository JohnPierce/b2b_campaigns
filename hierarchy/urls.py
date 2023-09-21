# hierarchy/urls.py

from django.urls import path
from hierarchy.views import org_chart, org_chart_company, get_hier_groups_by_company

urlpatterns = [
    path('org_chart/', org_chart, name='org_chart'),
    path('org_chart_company/<int:company_id>/', org_chart_company, name='org_chart_company'),
    path('get-hier-groups-by-company/<int:company_id>/', get_hier_groups_by_company, name='get_hier_groups_by_company'),
    # ... other url patterns
]
