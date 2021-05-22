from .models import ClientInvoice, InvoiceLink
from rest_framework import serializers


class ClientInvoiceSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    invoice_link = serializers.SerializerMethodField(read_only=True)
    short_link = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = ClientInvoice
        fields = ('id', 'user', 'username', 'invoice_number','project_name','amount_charged', 'invoice_link', 'short_link')

    def get_username(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def get_invoice_link(self, obj):
        invoice_link_obj = InvoiceLink.objects.filter(invoice=obj).order_by('-id').first()
        if invoice_link_obj:
           return invoice_link_obj.invoice_link

    def get_short_link(self, obj):
        invoice_link_obj = InvoiceLink.objects.filter(invoice=obj).order_by('-id').first()
        if invoice_link_obj:
           return invoice_link_obj.short_link


class InvoiceLinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InvoiceLink
        fields = "__all__"

        