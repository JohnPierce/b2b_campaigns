from django.db import models
from django.apps import apps
from django.core.exceptions import ValidationError
from django.utils import timezone
from cdata.models import Contact, Company

# Create your models here.

class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    twitter_handle = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    personal_url = models.URLField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    github_url = models.URLField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)
    website_url = models.URLField(max_length=255, blank=True, null=True)
    company_url = models.URLField(max_length=255, blank=True, null=True)
    patent_url = models.URLField(max_length=255, blank=True, null=True)
    following = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.contact and self.following:
            return f'following {self.contact}'
        elif self.contact:
            return f'not following {self.contact}'
        else:
            return "No Contact"

class FollowUp(models.Model):
    id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    follow = models.BooleanField(default=False)
    follow_up_type = models.CharField(max_length=255)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)


    def clean(self):
        if self.date < timezone.now().date():
            raise ValidationError('Date cannot be in the past')

    def __str__(self):
        return f'{self.contact.name} - {self.date} - {self.follow_up_type}'