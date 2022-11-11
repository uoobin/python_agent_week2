from django.db import models

# Create your models here.
class TransactionData(models.Model):
    timestamp = models.IntegerField()
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=50)
    status_code = models.IntegerField()
    latency = models.FloatField()

class UsageData(models.Model):
    cpu = models.FloatField()
    ram = models.IntegerField()

class SearchData(models.Model):
    timestamp = models.IntegerField()
