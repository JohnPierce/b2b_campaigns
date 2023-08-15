"""b2b_campaigns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # new
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from cdata.views import ContactViewSet, CompanyViewSet
from cdata.views import CompanyGroupViewSet, CompanyWithGroupHierarchyViewSet
from cdata.views import CompanyWithEmployeeHierarchyViewSet
from hierarchy.views import CompanyGroupHierarchyViewSet, EmployeeHierarchyViewSet
#from . import views as project_views  # Import views from your project for debugging



router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'companies', CompanyViewSet )
router.register(r'companygrouphierarchies', CompanyGroupHierarchyViewSet )
router.register(r'employeehierarchies', EmployeeHierarchyViewSet )
router.register(r'companygroups', CompanyGroupViewSet )
router.register(r'companieswithgrouphierarchies', CompanyWithGroupHierarchyViewSet, basename='companieswithgrouphierarchies')
router.register(r'compcontemphier', CompanyWithEmployeeHierarchyViewSet, basename='compcontemphier')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # new
    #path('print-router-urls/', project_views.print_router_urls),  # for debugging
    path('cdata/', include('cdata.urls')), # new
    #path('hierarchy/', include('hierarchy.urls')), # new, need to define urls and views
    #path('design_flow/', include('design_flow.urls')), # new, need to define urls and views
    #path('follow/', include('follow.urls')), # new, need to define urls and views
    path('', include('django.contrib.auth.urls')), # new

 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # new

admin.site.site_header = "B2B Campaigns Admin"
admin.site.site_title = "B2B Campaigns Admin Portal"
admin.site.index_title = "Welcome to B2B Campaigns Portal"
