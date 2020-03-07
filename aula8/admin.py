from django.contrib import admin
from .models import Pet
from datetime import datetime
from .forms import PetForm

class PetAdmin(admin.ModelAdmin):
    fields = ('nome', 'data_nascimento', 'ativo')
    list_display = ('nome', 'data_nascimento', 'show_name_and_year','ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    form = PetForm

    def show_name_and_year(self, obj):
        return obj.nome + " " + obj.data_nascimento.today().strftime("%m/%d/%y")

    def starts_with_b(self, obj):
        return obj.nome.startswith("b")
        

admin.site.register(Pet, PetAdmin)