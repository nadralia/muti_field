from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions, status
from .serializers import InquirySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from api.apps.accounts.models import User, Client, Company, CompanyTeamMember
from .models import Inquiry

# Create your views here.

class ListCreateInquiryView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = InquirySerializer

    def post(self, request, **kwargs):
        #get raw data
        client_raw_data = request.data.get('client', {})
        inquiry_raw_data = request.data.get('inquiry', {})

        #get current user 
        current_user = request.user
        user = get_object_or_404(User, email=current_user)
        companymember =  CompanyTeamMember.objects.get(user_id=user.id)

        company = Company.objects.get(id = companymember.company_id)

        client_raw_data['user'] = user
        client_raw_data['company'] = company
        client = Client.objects.create(**client_raw_data)

        #creating inquiry
        serializer = self.serializer_class(data=inquiry_raw_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, client=client, company=company)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request, **kwargs):
        """Get inquiries of a client"""
        current_user = request.user
        user = get_object_or_404(User, email=current_user)
        companymember =  CompanyTeamMember.objects.get(user_id=user.id)

        inquiries = Inquiry.objects.filter(company_id=companymember.company_id).select_related('client')

        serializer = self.serializer_class(inquiries, many=True)

        return Response(data={"inquiries":serializer.data}, status=status.HTTP_200_OK)


class UpdateDestroyInquiryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    
    def destroy(self, request, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            data={"message": "Inquiry deleted Successfully"},
            status=status.HTTP_200_OK,
        )

    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, pk):
        pass

