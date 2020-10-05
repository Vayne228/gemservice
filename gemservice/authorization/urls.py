from django.urls import path

from .views import *

urlpatterns = [
	path('', start_page, name='start_page_url'),
]