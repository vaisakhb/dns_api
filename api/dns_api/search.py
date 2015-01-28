from django.http import HttpResponse, Http404
from django.core import serializers
import re, json, xml
from getdata.models import record_search
from django.template import Context, RequestContext
def validation(request):
	limit = 30
	page = 1
	if request.method == "GET":
		pattern_validation1 = re.compile("^.*\.$")
		##Capture parameters
		type_of_record = request.GET.get('class')
		domain = request.GET.get('name')
		data = request.GET.get('data')
		ttl = request.GET.get('ttl')
		if request.GET.get('limit'):
			limit = int(request.GET.get('limit'))
		if request.GET.get('page'):
			page = int(request.GET.get('page'))
		limit_start = limit * page - limit
		limit_end = limit * page
		if not domain and not data:
			return HttpResponse("Invalid request. Mandatory parameters are ?name=xyz or ?data=xyz. Available parameters are ?name, ?data, ?ttl, ?class.", status=400)
		params = {"domain": domain, "record": type_of_record, "record_points_to": data, "ttl": ttl }
		params = dict((key, value) for key, value in params.iteritems() if value)
		response = search(params, limit_start, limit_end, page)
		if response:
			return HttpResponse(response)
		else:
			return HttpResponse("Record not found", status=404)
	else:
		return HttpResponse("Request method should be GET", status=405)
def date_handler(obj):
	return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def search(params, limit_start, limit_end, page):
	return_dict = {}
	filter_kwargs = {}
	for key,value in params.iteritems():
		filter_kwargs[key + "__startswith"] = value
	query_count = record_search.objects.filter(**filter_kwargs).only("domain", "record", "record_points_to", "priority_mx", "ttl", "generated_on").count()
	query_data = record_search.objects.filter(**filter_kwargs).only("domain", "record", "record_points_to", "priority_mx", "ttl", "generated_on")[limit_start:limit_end]
	query_data_length = {"records_returned":	len(query_data.values()), "total_records": query_count, "page": page}
	if query_data:
		data = list(query_data.values())
		return_dict["records"] = data
		return_dict["meta"] = query_data_length
		return_dict = json.dumps(return_dict, default=date_handler)
	else:
		return query_data
#	data = re.sub("\]$", query_data_length, data)
#	return re.sub('\"model\"\:\s+?\"getdata\.record_search\"\,', "", data) 
	return return_dict
