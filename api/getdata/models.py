from django.db import models


# Create your models here.
class record_search(models.Model):
	domain = models.CharField(max_length=100)
	record = models.CharField(max_length=100)
	record_points_to = models.CharField(max_length=100)
	priority_mx = models.CharField(max_length=100)
	ttl = models.CharField(max_length=100)
	#generated_on = models.CharField(max_length=100)
	generated_on = models.DateField()


class record_search_ptr(models.Model):
	ip = models.CharField(max_length=100)
	record = models.CharField(max_length=100)
	ip_points_to = models.CharField(max_length=100)
	ttl = models.CharField(max_length=100)
	generated_on = models.DateField()

