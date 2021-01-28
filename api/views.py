from django.shortcuts import render
from rest_framework import generics, permissions
from quotes.models import QuoteCategory, Quote, Country
from .serializers import QuoteSerializer, QuoteCategorySerializer, CountyrSerializer


class QuoteAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer


class CountryAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountyrSerializer


class QuoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteAPINewView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')[:1]
    serializer_class = QuoteSerializer
