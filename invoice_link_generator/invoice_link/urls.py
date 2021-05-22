from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client-invoice', views.ClientInvoiceViewSet, basename='client_invoice')
router.register('invoice-link', views.InvoiceLinkViewSet, basename='invoice_link')

urlpatterns = [
	path('signin/', views.SignUpPage.as_view(), name='sign_in_page'),
	path('login/', views.CustomObtainAuthToken.as_view(), name='api_login'),
	path('logout/', views.UserLogout.as_view(), name='api_logout'),

]

urlpatterns += router.urls