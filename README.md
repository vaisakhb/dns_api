# dns_api
An http api that queries mysql db and returns by default json.
Eg. url
http://Domain.com:port/search?name=testdomain&TTL=3600&class=CNAME
could give response 
```
[
    {
        "pk": 17965,
        "fields": {
            "domain": "testdomain.com.\n",
            "priority_mx": "NA",
            "generated_on": "2015-01-25T03:21:12",
            "record": "CNAME",
            "ttl": "3600",
            "record_points_to": "testdomain.cname.com.\n"
        }
    },
    {
        "Total records": 1
    }
]
```
To check how many CNAMES are pointing to a domain, use 
http://Domain.com:port/search?data=testdomain-cname&class=CNAME
can give 
```
[
    {
        "pk": 17965,
        "fields": {
            "domain": "testdomain.com.\n",
            "priority_mx": "NA",
            "generated_on": "2015-01-25T03:21:12",
            "record": "CNAME",
            "ttl": "3600",
            "record_points_to": "testdomain-cname.com.\n"
        }
    },
    {
        "pk": 17965,
        "fields": {
            "domain": "anothertestdomain1.com.\n",
            "priority_mx": "NA",
            "generated_on": "2015-01-25T03:21:12",
            "record": "CNAME",
            "ttl": "3600",
            "record_points_to": "testdomain-cname.com.\n"
        }
    },
    {
        "Total records": 2
    },
    
]
```
