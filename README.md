# dns_api
An http api written in Django that queries mysql db for stored dns records, and returns the matching record names in json by default.
Run record_dumper.py inside daemon to populate the database(thaw still in progress).
Eg:
`:8000/api/search?name=test&ttl=60`
could give response 
```
{
records: [
{
domain: "testdomain.com",
priority_mx: "NA",
generated_on: "2015-01-25T03:47:19",
record_points_to: "10.84.30.138",
record: "A",
ttl: "60",
id: 115
}
],
meta: {
total_records: 1,
records_returned: 1,
page: 1
}
}

```
To check how many CNAMES are pointing to a domain, use 
`:8000/api/search?data=testdomain-cname&class=CNAME`
can give 

```
{
records: [
{
domain: "domain1.com.",
priority_mx: "NA",
generated_on: "2015-01-25T03:47:19",
record_points_to: "testdomain-cname.com.",
record: "CNAME",
ttl: "3600",
id: 296
},
{
domain: "domain2.com.",
priority_mx: "NA",
generated_on: "2015-01-25T03:47:46",
record_points_to: "testdomain-cname.com.",
record: "CNAME",
ttl: "3600",
id: 17977
}
],
meta: {
total_records: 2,
records_returned: 2,
page: 1
}
}

```

Available parameters are
`:8000/api/search?data=testdomain-cname&class=CNAME&ttl=3600&name=domain1&limit=50&page=2`
