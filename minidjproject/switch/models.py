from django.db import models

# Create your models here.
class switch_details(models.Model):
	switch_model=models.CharField(max_length=100)
	switch_ip=models.CharField(max_length=100)
	netmask=models.CharField(max_length=100)
	gateway=models.CharField(max_length=100)
	mac_address=models.CharField(max_length=100)
