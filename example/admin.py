from django.contrib import admin
from .models import Pessoa, Filho

# Register your models here.
# admin.site.register(Pessoa)
# admin.site.register(Filho)
from .models import Pessoa, Filho

class FilhoInline(admin.TabularInline):
  model = Filho
  extra = 2

class PessoaAdmin(admin.ModelAdmin):
  # fieldsets = [
  #   (None, { "fields": ["Pessoa_text"] }),
  #   ("Date information", {
  #     "fields": ["pub_date"], "classes": ["collapse"]
  #   }),
  # ]
  model = Pessoa
  inlines = [FilhoInline]
  # list_display = ["Pessoa_text", "pub_date", "was_published_recently"]
  # list_filter = ["pub_date"]
  # search_fields = ["Pessoa_text"]

admin.site.register(Pessoa, PessoaAdmin)
