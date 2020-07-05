from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Contrato, Seguro, Vendedor, Institucion, Apoderado

# Register your models here.

admin.site.site_header = 'Agencia On-Tour'

admin.site.register(Contrato)
admin.site.register(Seguro)
admin.site.register(Vendedor)
admin.site.register(Institucion)
admin.site.register(Apoderado)