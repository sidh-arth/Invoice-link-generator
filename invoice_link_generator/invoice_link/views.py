from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate

from rest_framework import viewsets, status, filters, serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ClientInvoice, InvoiceLink
from .serializers import ClientInvoiceSerializer, InvoiceLinkSerializer
# Create your views here.



class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
        except Exception as e:
            response_data = {
                'status_code': "400",
                'status': False,
                'message': "Invalid Username/Password"
            }
        else:
            token, created = Token.objects.get_or_create(user=user)
            if created:
                login_data = { 'id': user.id,  'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email, 'token': token.key }
                response_data = {
                    'status_code': "200",
                    'status': True,
                    'message': "Logged in successfully",
                    'data': login_data
                }
            else:
                response_data = {
                    'status_code': "400",
                    'status': False,
                    'message': "User already logged in! Please log out from all your active sessions and try again",
                    'data': {"token": token.key, "is_user_already_logged_in": True}
                }
        if response_data['status_code'] == '400':
            response_status = status.HTTP_400_BAD_REQUEST
        elif response_data['status_code'] == '200':
            response_status = status.HTTP_200_OK
        return Response(response_data, status=response_status)


class UserLogout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        request.user.auth_token.delete() 
        response_data = {
            'status_code': "200",
            'status': True,
            'message': "User logged out successfully.",
        }
        return Response(response_data)


class ClientInvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ClientInvoice.objects.all()
    serializer_class = ClientInvoiceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response_data = {
            "status_code": "200",
            "status": True,
            "message": 'Invoice List',
            "data": data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            response = super().create(request)
        except Exception as e:
            print(str(e))
        response_data = {
            "status_code": "201",
            "status": True,
            "message": "Invoice record created successfully",
            "data": response.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class InvoiceLinkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = InvoiceLink.objects.all()
    serializer_class = InvoiceLinkSerializer