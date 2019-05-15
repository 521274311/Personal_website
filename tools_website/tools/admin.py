from django.contrib import admin
import xadmin
from .models.typemodels import Type
# Register your models here.
class TypeAdminModel(object):
    list_display = ['id', 'name', 'status', 'add_time', 'update_time', 'add_user']
    fields = ['name', 'status', 'parent']
    search_fields = ['name', 'parent']


xadmin.site.register(Type, TypeAdminModel)