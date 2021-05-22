from django.apps import AppConfig


class InvoiceLinkConfig(AppConfig):
    name = 'invoice_link'

    def ready(self):
        import invoice_link.signals

