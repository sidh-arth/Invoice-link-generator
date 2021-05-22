from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
# Create your models here.


class ObjManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

        
class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Updated Time')
    objects = ObjManager()
    original_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.save()


class ClientInvoice(BaseModel):
    """ClientInvoice ::  Contains details of the Invoices related to a user """
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=13, unique=True)
    project_name = models.CharField(max_length=255, null=True, blank=True)
    amount_charged = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.firstname + ' ' + self.user.lastname + ' - ' +self.invoice_number 


class InvoiceLink(BaseModel):
    """InvoiceLink :: Contains all the links that are generated against each invoices """
    invoice = models.ForeignKey(ClientInvoice, null=True, blank=True, on_delete=models.CASCADE, related_name='invoice_details')
    invoice_link = models.CharField(max_length=255, unique=True)
    shared_with_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.invoice.user.firstname + ' ' + self.invoice.user.lastname + ' - ' +self.invoice_link 