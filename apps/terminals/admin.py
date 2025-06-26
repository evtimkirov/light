from django.contrib import admin
from .models import Terminal
from ..accessories.models import Accessory


class AccessoryInline(admin.TabularInline):  # or admin.StackedInline
    model = Accessory
    extra = 1

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'in_stock', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('in_stock', 'created_at')
    inlines = (AccessoryInline, )
