from rest_framework import serializers
from quotes.models import Quote, QuoteCategory, Country


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('__all__')


class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory
        fields = ('__all__')


class CountyrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('__all__')

