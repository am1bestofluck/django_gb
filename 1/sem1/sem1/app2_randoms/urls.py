from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('assassination/', views.assassination, name='assassination'),
    path('get_coins/<int:qua>', views.get_coins, name='qet_coins'),
    path('throw_coins/<int:qua>', views.ThrowAllCoins.as_view(), name="throw_coins")
]
