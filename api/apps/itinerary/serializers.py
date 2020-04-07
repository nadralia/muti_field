from rest_framework import serializers, status
from .models import *


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Activity
        fields = [
            'id',
            'title',
            'description',
        ]



class DaySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    activities = ActivitySerializer(many=True)

    class Meta:
        model = Day
        fields = [
            'id',
            'daytype',
            'activity',
        ]
        read_only_fields = ('activity',)



class ItinerarySerializer():
    id = serializers.IntegerField(required=False)
    itinerarystatus = serializers.IntegerField(required=False)
    days = DaySerializer(many=True)

    class Meta:
        model = Itinerary
        fields = [
            'id',
            'description',
            'itinerarystatus',
            'inquiry',
            'day'
        ]
        depth = 2
        read_only_fields = ('inquiry', 'day')

