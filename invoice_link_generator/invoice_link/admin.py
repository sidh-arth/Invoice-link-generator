from django.contrib import admin
from .models import ClientInvoice, InvoiceLink
# Register your models here.

admin.site.site_header = "Client Invoice Generator Admin Portal"
admin.site.site_title = "CIG Portal"
admin.site.index_title = "Welcome to Client Invoice Generator Admin Portal"


admin.site.register(ClientInvoice)
admin.site.register(InvoiceLink)