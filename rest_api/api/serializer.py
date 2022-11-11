from rest_framework import serializers
from api.models import TransactionData, UsageData, SearchData

class TransactionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionData
        fields = '__all__'

class UsageDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = UsageData
        fields = '__all__'

class SearchDataSerializer(serializers.ModelSerializer) :
    class Meta :
        model = SearchData
        fields = '__all__'