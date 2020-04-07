from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions, status
from .serializers import ItinerarySerializer
from rest_framework.response import Response
from .models import Itinerary
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from api.apps.inquiry.models import Inquiry

# Create your views here.

class ListCreateItineraryAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ItinerarySerializer

    def post(self, request, **kwargs):
        itineray_data = request.data.get('itinerary', {})

        #get all the day lists
        days =  itineray_data.pop('days')

        print('***** Days:', days)

        #get all the activities in the day
        activities = days.pop('activity')

        print('***** Activities:', activities)

        

    def get(self, request, **kwargs):
        """Get itineraries of a company"""
        pass



class UpdateDestroyItineraryAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ItinerarySerializer
    
    def destroy(self, request, **kwargs):
        pass

    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, slug, pk):
        pass
