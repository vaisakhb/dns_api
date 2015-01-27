from django.http import HttpResponse, Http404
from django.core import serializers
import re, json, xml
from getdata.models import record_search
from django.template import Context, RequestContext
def validation(request):
	offset = 30
	page = 1
	if request.method == "GET":
		pattern_validation1 = re.compile("^.*\.$")
		##Capture parameters
		type_of_record = request.GET.get('class')
		domain = request.GET.get('name')
		data = request.GET.get('data')
		ttl = request.GET.get('ttl')
		if request.GET.get('offset'):
			offset = int(request.GET.get('offset'))
		if request.GET.get('page'):
			page = int(request.GET.get('page'))
		limit_end_offset = offset * page
		limit_start_offset = offset * page - offset
		if not domain and not data:
			return HttpResponse("Invalid request. Mandatory parameters are ?name=xyz or ?data=xyz. Available parameters are ?name, ?data, ?ttl, ?class.", status=400)
		params = {"domain": domain, "record": type_of_record, "record_points_to": data, "ttl": ttl }
		params = dict((key, value) for key, value in params.iteritems() if value)
		response = search(params, limit_start_offset, limit_end_offset, page)
		if response:
			return HttpResponse(response)
		else:
			return HttpResponse("Record not found", status=404)
	else:
		return HttpResponse("Request method should be GET", status=405)
def date_handler(obj):
	return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def search(params, limit_start_offset, limit_end_offset, page):
	filter_kwargs = {}
	for key,value in params.iteritems():
		filter_kwargs[key + "__startswith"] = value
	query_count = record_search.objects.filter(**filter_kwargs).only("domain", "record", "record_points_to", "priority_mx", "ttl", "generated_on").count()
	query_data = record_search.objects.filter(**filter_kwargs).only("domain", "record", "record_points_to", "priority_mx", "ttl", "generated_on")[limit_start_offset:limit_end_offset]
	query_data_length = {"records_returned":	len(query_data.values()), "total_records": query_count, "page": page}
	if query_data:
		data = list(query_data.values())
		data.insert(0, query_data_length)
		data = json.dumps(data, default=date_handler)
	else:
		return query_data
#	data = re.sub("\]$", query_data_length, data)
#	return re.sub('\"model\"\:\s+?\"getdata\.record_search\"\,', "", data) 
	return data

