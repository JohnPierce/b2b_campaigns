from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view, name='home'),
    #path('companies/', views.companies, name='companies'),
    #path('suppliers/', views.suppliers, name='suppliers'),
    #path('company_supplier_spend/', views.company_supplier_spend, name='company_supplier_spend'),
    #path('eda_design_flow/', views.eda_design_flow, name='eda_design_flow'),
    #path('semiconductor_fpga_platform/', views.semiconductor_fpga_platform, name='semiconductor_fpga_platform'),
    #path('signup/', views.SignUpView.as_view(), name='signup'),
]