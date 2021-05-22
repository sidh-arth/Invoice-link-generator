from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ClientInvoice, InvoiceLink
from django.conf import settings
from invoice_link_generator.settings import PAYMENT_BASE_URL, BITLY_GROUP, BITLY_TOKEN
from urllib.parse import urlencode
from urllib.request import urlopen
import requests

@receiver(post_save, sender=ClientInvoice)
def generate_short_link(sender, instance, created, **kwargs):
    if created:
        unique_link = PAYMENT_BASE_URL + instance.invoice_number +'/'   #replace the line with logic for payment url

        print(PAYMENT_BASE_URL, ' \n\n ', unique_link, ' \n\n ', BITLY_GROUP, ' ======================\n\n')

        # endpoint = 'https://api-ssl.bitly.com/v3/shorten?access_token={0}&longUrl={1}&format=txt'
        # print(endpoint.format(BITLY_KEY, unique_link), ' \n\n\n')
        # req = urlencode(endpoint.format(BITLY_KEY, unique_link))
        # print(123,'\n\n')
        # short_url = urlopen(req).read()

        print(unique_link)
        headers = { 'Authorization': 'Bearer '+BITLY_TOKEN, 'Content-Type': 'application/json' }
        data = { "long_url": unique_link, "domain": "bit.ly", "group_guid": BITLY_GROUP }
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

        

        # payload = {"group_guid": BITLY_GROUP,  "domain": "bit.ly",  "long_url": unique_link }  
        # response = requests.post(endpoint, data = payload)
        print(response.__dict__,' ====================== ')

        # print(short_url, ' ================')
        # invoice_detail_entry = InvoiceLink.objects.create(invoice=instance, payment_link=unique_link, short_link=short_url)





        
