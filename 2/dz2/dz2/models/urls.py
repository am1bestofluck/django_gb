from django.urls import path
from . import views

urlpatterns = [
    path('orderlog/<int:customer_id>', views.OrderLog.as_view(), name='order_log')
]
