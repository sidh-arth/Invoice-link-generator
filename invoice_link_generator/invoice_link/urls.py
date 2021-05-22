from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client-invoice', views.ClientInvoiceViewSet, basename='client_invoice')

urlpatterns = [
	path('login/', views.CustomObtainAuthToken.as_view(), name='api_login'),
	path('logout/', views.UserLogout.as_view(), name='api_logout'),
]

urlpatterns += router.urls