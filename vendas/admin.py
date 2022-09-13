from django.contrib import admin

from .models import Venda, ItemVenda


class ItemVendaAdmin(admin.TabularInline):
    model = ItemVenda
    extra = 0


class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaAdmin]
    class Meta:
        model = Venda


admin.site.register(Venda, VendaAdmin)
