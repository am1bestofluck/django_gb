import pdb

from django.contrib import admin

# Register your models here.

from .models import Client, Order, Ware


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Client._meta.fields]
    list_display_links = ['name']
    readonly_fields = ['id', 'date_reg']
    # pdb.set_trace()
    fieldsets = (('personal', {'fields': ['name', 'mail', 'phone', 'path'],
                               'description': 'stick to read-only, unless ASSURED'}),
                 ('support', {'fields': readonly_fields, 'classes': ['collapse'],
                              'description': 'why bother ;]'}))


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Order._meta.fields]
    list_display_links = ['client']
    readonly_fields = ['id']
    fieldsets = (('basic', {'fields': ['id', 'client', 'date_locked']}),
                 ('positions', {'fields': ['wares','total'],
                                'classes': ['collapse'],
                                'description': 'джанго против ManyToManyField, очевидно =\\;'
                                               'была бы неделька в запасе - может и написал бы обход.'
                                               'Вроде как есть методичка в документации;'
                                               'А так - имеем то что имеем'
                                }))


@admin.register(Ware)
class WareAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Ware._meta.fields]
    list_display_links = ['title']

    readonly_fields = ['id', 'date_income']

    fieldsets = (
        ('Basic', {'fields': ['title', 'notes', 'price', 'quantity', 'date_income']}),
        ('preview', {'fields': ['front_view'], 'classes': ['collapse in'],
                     'description': 'На самом деле идея была в том чтобы вывести превью; но тут надо кроить шаблон...'
                                    ' наверно не успеваю =\\'}))
