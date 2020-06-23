from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao', 'usuario')
    list_filter = ('titulo','data_evento','usuario',)

admin.site.register(Evento, EventoAdmin)
