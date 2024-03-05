from django.contrib import admin
from .models import CostEntry


class FormAdmin(admin.ModelAdmin):
    list_display = ('date', 'cost_for', 'cost_group', 'price')
    search_fields = ('date', 'cost_for')
    list_filter = ('date', 'cost_group')


admin.site.register(CostEntry, FormAdmin)
