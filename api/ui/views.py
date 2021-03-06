from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404, HttpRequest
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.views.decorators.csrf import csrf_exempt
import urllib, json, HTMLParser, socket, re, pprint, collections
from django.core import serializers
import yaml, os
from itertools import izip
import requests
myhost = socket.gethostname()
cwd = os.path.dirname(__file__)

with open(cwd + "/config.yaml",'r') as f:
	config_yaml=yaml.load(f)
try:
        write_api=config_yaml["WRITE_API"]
except KeyError:
        print "Config parameters not found "
        raise SystemExit

username = "Anonymouse"
def search_template(request):
	global username
#	username = request.user.username
	if 'REMOTE_USER' in request.META:
		username = request.META['REMOTE_USER'] 
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

def compare(a, b):
	return set(a) == set(b) and len(a) == len(b)

@csrf_exempt
def update_data(request):
	new_dict = {}
	old_dict = {}
	return_dict = {}
	#array = []
	for key, value in request.POST.iterlists():
		if key.startswith("new"):
			new_dict[key] = [str(x) for x in value]
		elif key.startswith("old"):
			key = re.sub("old", "new", key)
			old_dict[key] = [str(x) for x in value]
		elif key.startswith("currenturl"):
			return_dict[key] = [str(x) for x in value]
	for key, value in new_dict.iteritems():
		if not compare(new_dict[key], old_dict[key]):
			return_dict[key] =  value
			return_dict[re.sub("new", "old", key)] = old_dict[key]
#	return HttpResponse(return_dict.values())
	return render_to_response('confirm.html', {"return_dict": sorted(return_dict.iteritems())})


@csrf_exempt
def callapi(request):
	new_dict = {}
	new_dict["add"] = []
	old_dict = {}
	old_dict["delete"] = []
	return_dict = {}
	name_array = ["name", "data", "class", "ttl"]
	for key, value in request.POST.iterlists():
		if key.startswith("new"):
			tmpstr = "".join([str(x) for x in value])
			try: 
				i = iter(name_array)
				b = dict(izip(i, tmpstr.split(",")))
				
				new_dict["add"].append(b)
			except:
				return HttpResponse("error")
		elif key.startswith("old"):
			tmpstr = "".join([str(x) for x in value])
			try:
				i = iter(name_array)
				b = dict(izip(i, tmpstr.split(",")))
				old_dict["delete"].append(b)
			except:
				return HttpResponse("error")
	post_data = dict(new_dict)
	post_data.update(old_dict)
	payload = json.dumps(post_data)
	r = requests.post(write_api, auth=('girish.g', 'Test234'), data=payload)
	return HttpResponse(r)
