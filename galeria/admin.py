from django.contrib import admin
from galeria.models import Fotografia


@admin.register(Fotografia)
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
