from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_start(request):
	return redirect('start_page_url', permanent=True)