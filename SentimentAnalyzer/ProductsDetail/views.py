# from django.shortcuts import render
from rest_framework import generics
# from rest_framework.response import Response
from ProductsDetail.serializers import ProductSerializer, ReviewSerializer 
from ProductsDetail.models import Product, Review


class listView(generics.ListAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
