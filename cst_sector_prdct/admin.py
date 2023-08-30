from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Sector, Industry, VerticalMarket, Application, Algorithm  # new
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector', 'description')
    search_fields = ('name', 'sector__name', 'description')
    ordering = ('sector', 'name')

class VerticalMarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'description')
    search_fields = ('name', 'industry__name', 'description')
    ordering = ('industry', 'name')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'vertical_market', 'description')
    search_fields = ('name', 'vertical_market__name', 'description')
    ordering = ('vertical_market', 'name')

class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('name', 'application', 'description')
    search_fields = ('name', 'application__name', 'description')
    ordering = ('application', 'name')

admin.site.register(Sector, SectorAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(VerticalMarket, VerticalMarketAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Algorithm, AlgorithmAdmin)