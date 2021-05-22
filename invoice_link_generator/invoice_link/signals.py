from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ClientInvoice, InvoiceLink
from django.conf import settings
from invoice_link_generator.settings import PAYMENT_BASE_URL, BITLY_GROUP, BITLY_TOKEN
from .utils import generate_short_url

@receiver(post_save, sender=ClientInvoice)
def generate_short_link(sender, instance, created, **kwargs):
    if created:
        unique_link = PAYMENT_BASE_URL + instance.invoice_number +'/'   #replace the line with logic for payment url
        short_link = generate_short_url(bitly_token=BITLY_TOKEN, bitly_group=BITLY_GROUP, unique_link=unique_link)
        if short_link:
            status = InvoiceLink.objects.create(invoice=instance , payment_link=unique_link , short_link=short_link)
        else:
            status = InvoiceLink.objects.create(invoice=instance , payment_link=unique_link)




        
