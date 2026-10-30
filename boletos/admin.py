
from django.contrib import admin
from .models import Emitente, Pagador, Boleto


admin.site.register(Emitente)
admin.site.register(Pagador)
admin.site.register(Boleto)

