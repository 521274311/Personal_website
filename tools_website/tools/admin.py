from django.contrib import admin
import xadmin
from .models.typemodels import Type
from .models.toolmodels import Tool
# Register your models here.
class TypeAdminModel(object):
    list_display = ['id', 'name', 'status', 'add_time', 'update_time', 'add_user']
    fields = ['name', 'status', 'parent']
    search_fields = ['name', 'parent']

class ToolAdminModel(object):
    list_display = ['id', 'tool_link', 'tag', 'add_time', 'update_time', 'add_user']
    fields = ['tool_link', 'tag']
    search_fields = ['tool_link', 'tag']

xadmin.site.register(Type, TypeAdminModel)
xadmin.site.register(Tool,ToolAdminModel)