from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404, HttpRequest
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.views.decorators.csrf import csrf_exempt
import urllib, json, HTMLParser, socket
myhost = socket.gethostname()
username = "Anonymouse"

def search_template(request):
	return render_to_response('base.html', {"username" : username})
	
def search_data(request):
	page = 1
	type_of_record = request.GET.get('type')
	if request.GET.get('page'):
		page = request.GET.get('page')
	if request.GET.get('data'):
		search_data = request.GET.get('data')
		result = search_cname(request.GET.get('data'), type_of_record, str(page))
	if request.GET.get('q'):
		search_name = request.GET.get('q')
		result = search_A(request.GET.get('q'), type_of_record, str(page))
#	else:
#		result = search_A(request.GET.get('q'))
	myserver_domain = "http://" + myhost + ":8000/ui/search/"
	return render_to_response('search.html', {"search" : result, "username" : username, "myserver_domain" : myserver_domain})

def search_cname(request, type_of_record, page):
	url = "http://" + myhost + ":8000/api/search?data=" + request + "&class=" + type_of_record + "&page=" + page
	u = urllib.FancyURLopener(None)
	usock = u.open(url)
	rawdata = usock.read()
	usock.close()
	return rawdata	

def search_A(request, type_of_record, page):
	url = "http://" + myhost + ":8000/api/search?name=" + request + "&class=" + type_of_record + "&page=" + page
	u = urllib.FancyURLopener(None)
	usock = u.open(url)
	rawdata = usock.read()
	usock.close()
	return rawdata


@csrf_exempt
def update_data(request):
	POST = request.POST
	return HttpResponse(POST)
