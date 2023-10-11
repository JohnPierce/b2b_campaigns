from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('get-groups-by-company/<int:company_id>/', views.get_groups_by_company, name='get_groups_by_company'),
    path('get-office-location-by-company/<int:company_id>/', views.get_office_location_by_company, name='get_office_location_by_company'),
    path('get-edadesignflowsubcategory-by-edadesignflow/<int:edadesignflow_id>/', views.get_edadesignflowsubcategory_by_edadesignflow, name='get_edadesignflowsubcategory_by_edadesignflow'),
    path('get-edasuppliertools-by-edadesignflow/<int:edadesignflow_id>/', views.get_edasuppliertools_by_edadesignflow, name='get_edasuppliertools_by_edadesignflow'),
    path('get-edasuppliertools/', views.get_edasuppliertools, name='get_edasuppliertools'),
    #path('companies/', views.companies, name='companies'),
    #path('suppliers/', views.suppliers, name='suppliers'),
    #path('company_supplier_spend/', views.company_supplier_spend, name='company_supplier_spend'),
    #path('eda_design_flow/', views.eda_design_flow, name='eda_design_flow'),
    #path('semiconductor_fpga_platform/', views.semiconductor_fpga_platform, name='semiconductor_fpga_platform'),
    #path('signup/', views.SignUpView.as_view(), name='signup'),
]
