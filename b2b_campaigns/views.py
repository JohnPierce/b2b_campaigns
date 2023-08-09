# views.py in your project directory for debugging:

from django.http import HttpResponse
from .urls import router  # Import the router from your project's urls.py

def print_router_urls(request):
    print(router.urls)
    return HttpResponse("Router URLs printed to console.")
