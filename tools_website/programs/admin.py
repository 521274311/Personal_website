from django.contrib import admin
# import xadmin
from .models.languagemodels import Language
from .models.linkmodels import Link
# Register your models here.
@admin.register(Language)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'version', 'status', 'add_time', 'update_time')
    fields = ('name', 'version', 'status')

    # def save_model(self, request, obj, form, change):
    #     obj.status = 0
    #     super().save_model(request, obj, form, change)

@admin.register(Link)
class LinkModelAdmin(admin.ModelAdmin):
    list_display = ('l_language', 'url', 'status', 'add_time', 'update_time')
    fields = ('l_language', 'url', 'status')

    # def save_model(self, request, obj, form, change):
    #     pass