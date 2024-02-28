from django.urls import path
from . import views

urlpatterns = [
    path('orderlog/<int:customer_id>', views.OrderLog.as_view(), name='order_log'),
    path("", views.index, name="shortcut"),
    path('r_u_ware/<int:ware_id>', views.EditWare.as_view(), name="r_u_ware"),

]
