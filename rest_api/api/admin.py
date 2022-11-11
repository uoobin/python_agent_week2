from django.contrib import admin
from api.models import TransactionData, UsageData, SearchData

# Register your models here.
admin.site.register(TransactionData)
admin.site.register(UsageData)
admin.site.register(SearchData)