from django.http import HttpResponse, Http404
from django.core import serializers
import re, json, xml
from getdata.models import record_search
from django.template import Context, RequestContext
LANG_DEFAULT = "json"
def validation(request):
	lang = LANG_DEFAULT
	if request.method == "GET":
		pattern_validation1 = re.compile("^.*\.$")
		##Capture parameters
		type_of_record = request.GET.get('class')
		domain = request.GET.get('name')
		data = request.GET.get('data')
		ttl = request.GET.get('ttl')

		if request.GET.get('lang'): 
			lang = request.GET.get('lang')
		params = {"domain": domain, "record": type_of_record, "record_points_to": data, "ttl": ttl }
		params = dict((key, value) for key, value in params.iteritems() if value)
		if  domain and pattern_validation1.search(domain):
			return HttpResponse("Domain name should not end with a trailing dot '.'", status=400)
		else:
			response = search(params, lang)
			if response:
				return HttpResponse(search(params, lang))
			else:
				return HttpResponse("Record not found", status=404)
	else:
		return HttpResponse("Request method should be GET", status=405)

def search(params, lang):
	filter_kwargs = {}
	for key,value in params.iteritems():
		filter_kwargs[key + "__startswith"] = value
	query_data = record_search.objects.filter(**filter_kwargs).only("domain", "record", "record_points_to", "priority_mx", "ttl", "generated_on")
	query_data_length = ', {"Total records": ' +	str(len(query_data.values())) + '}]';
	if query_data:
		data = serializers.serialize(lang, query_data)
	else:
		return query_data
	data = re.sub("\]$", query_data_length, data)
	return re.sub('\"model\"\:\s+?\"getdata\.record_search\"\,', "", data) 
	





"""
	if request.method == "GET":
		pattern_validation1 = re.compile("^.*\.$")
		if pattern_validation1.search(pattern):
			return HttpResponse("Query string should not end with a trailing dot '.'", status=400)
		else:
			return search_keyword(pattern)
	else:
		response = "Request method should be GET"
		return HttpResponse(response, status=405)

def search_keyword(pattern):
	from getdata.models import RECORD_SEARCH
	record_list = RECORD_SEARCH.objects.filter(domain__startswith=pattern)
	data = serializers.serialize("json", record_list)
	
	#record_list = RECORD_SEARCH.objects.filter(domain__startswith=pattern).values()
#	return HttpResponse("OOMBI", status=200)
	if not record_list:
		return HttpResponse("Query string not found", status=404)
	else:
		#return HttpResponse(record_list.values(), status=200)
		return HttpResponse(data, status=200)
		#return HttpResponse(serializers.serialize("json",record_list.values(), status=200))
		#return HttpResponse(records, status=200)
"""
