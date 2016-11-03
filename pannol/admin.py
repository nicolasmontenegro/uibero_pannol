from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import models


class InfoProductoFilter(admin.SimpleListFilter):
    title = _('precio')
    parameter_name = 'precio'
    def lookups(self, request, model_admin):        
        return (
            ('0-9999', _('menor que $10.000')),
            ('10000-99999', _('entre $10.000 y $99.999')),
            ('100000--inf', _('mayores o igual a $100.000')),
        )

    def queryset(self, request, queryset):        
        if self.value() == '0-9999':
            return queryset.filter(valor__lt=10000)
        if self.value() == '10000-99999':
            return queryset.filter(valor__gte=10000, valor__lt=100000)
        if self.value() == '10000-99999':
            return queryset.filter(valor__gte=100000)

class InfoProductoAdmin(admin.ModelAdmin):
    fields = ('nombre', 'marca', 'modelo', 'valor') 
    list_display = ('nombre', 'marca') 
    list_filter = ('marca', InfoProductoFilter)
    ordering = ('-nombre',)

admin.site.register(models.InfoProducto, InfoProductoAdmin)
admin.site.register(models.Estudiante)
admin.site.register(models.Producto)
admin.site.register(models.Prestamo)