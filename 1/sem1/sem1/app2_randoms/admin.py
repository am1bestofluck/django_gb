from django.contrib import admin
from .models import CoinLogger


# Register your models here.

@admin.register(CoinLogger)
class CoinLoggerAdmin(admin.ModelAdmin):
    pass
