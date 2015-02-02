from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
import urllib, json, HTMLParser, socket
myhost = socket.gethostname()
username = "Anonymouse"

def search_template(request):
	return render_to_response('home.html', {"username" : username})
	
def search_data(request):
	type_of_record = request.GET.get('type')
	if type_of_record == "CNAME":
		result = search_cname(request.GET.get('q'))
	else:
		result = search_A(request.GET.get('q'))
	return render_to_response('search.html', {"search" : result, "username" : username})

def search_cname(request):
	url = "http://" + myhost + ":8000/api/search?data=" + request
	u = urllib.FancyURLopener(None)
	usock = u.open(url)
	rawdata = usock.read()
	usock.close()
	return rawdata	

def search_A(request):
	url = "http://" + myhost + ":8000/api/search?name=" + request
	u = urllib.FancyURLopener(None)
	usock = u.open(url)
	rawdata = usock.read()
	usock.close()
	return rawdata
