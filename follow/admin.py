from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import SocialMedia
from .models import FollowUp
#from cdata.models import Contact, Company
from import_export.admin import ImportExportModelAdmin



# Register your models here
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('contact', 'associated_company', 'following', 'twitter_handle', 'linkedin_url', 'facebook_url', 'instagram_url', 'github_url', 'youtube_url', 'website_url')
    list_filter = ('following', 'twitter_handle', 'linkedin_url', 'facebook_url', 'instagram_url', 'github_url', 'youtube_url', 'website_url')
    search_fields = ('contact', 'associated_company', 'following', 'twitter_handle', 'linkedin_url', 'facebook_url', 'instagram_url', 'github_url', 'youtube_url', 'website_url')
    ordering = ('contact','following', 'twitter_handle', 'linkedin_url', 'facebook_url', 'instagram_url', 'github_url', 'youtube_url', 'website_url')

    def associated_company(self, obj):
        return obj.contact.company
    associated_company.short_description = 'Company'

class FollowUpAdmin(admin.ModelAdmin):
    list_display = ('contact', 'associated_company','follow', 'follow_up_type', 'date', 'notes')
    list_filter = ('follow', 'follow_up_type', 'date', 'notes')
    search_fields = ('contact', 'associated_company','follow', 'follow_up_type', 'date', 'notes')
    ordering = ('contact', 'follow', 'follow_up_type', 'date', 'notes')

    def associated_company(self, obj):
        return obj.contact.company
    associated_company.short_description = 'Company'






admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(FollowUp, FollowUpAdmin)
