from .models import ClientInvoice, InvoiceLink
from rest_framework import serializers


class ClientInvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClientInvoice
        fields = "__all__"


class InvoiceLinkSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = InvoiceLink
        fields = "__all__"

		