from django.contrib import admin
from django.contrib.admin import RelatedFieldListFilter
from django.utils.html import format_html

from main.models import Link, Agent


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'supplier', 'buyer', 'product', 'created_at', 'duty', 'view_supplier_link', 'supplier__city',
    )
    list_filter = ['supplier__city']
    actions = ['clear_duty']

    @admin.action(description="clear debet")
    def clear_duty(self, request, queryset):
        queryset.update(duty=0)

    def view_supplier_link(self, obj):
        return format_html(f'<a href="/admin/main/agent/{obj.supplier.id}/change">Поставщик: {obj.supplier.name}</a>')

    def supplier_city(self, obj):
        return obj.supplier.city

    supplier_city.short_description = 'Город продажи'


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('type_agent',
                    'name',
                    'email',
                    'country',
                    'city',
                    'street',
                    'house_number',
                    )