from django.contrib import admin
# import xadmin
from .models.languagemodels import Language
# Register your models here.
@admin.register(Language)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'version', 'status')
    fields = ('name', 'version')

    def save_model(self, request, obj, form, change):
        obj.status = 0
        super().save_model(request, obj, form, change)