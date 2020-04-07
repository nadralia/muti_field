from rest_framework import serializers, status
from .models import *
from api.apps.accounts.models import Client, CompanyTeamMember
from api.apps.accounts.serializers import ClientSerializer


class InquirySerializer(serializers.ModelSerializer):
    inquirystatus = serializers.IntegerField(required=False)

    class Meta:
        model = Inquiry
        fields = [
            'id',
            'client',
            'inquirystatus',
            'description'
        ]
        depth = 1
        read_only_fields = ('client',)
        