from django.contrib import admin
# import xadmin
from .models.typemodels import Type
from .models.toolmodels import Tool
# Register your models here.


class BaseAdminModel(object):
    def save_models(self):
        self.new_obj.add_user_id = self.request.user.id
        super().save_models()


class TypeAdminModel(BaseAdminModel):
    list_display = ['id', 'name', 'status', 'parent', 'add_time', 'update_time', 'add_user']
    fields = ['name', 'status', 'parent']
    search_fields = ['name', 'parent']

    def parent_list(self, request,queryset):
        pass

    def first_parent(self, obj):
        if obj.parent_id == None:
            return obj

class ToolAdminModel(BaseAdminModel):
    list_display = ['id', 'tool_link', 'tag', 'add_time', 'update_time', 'add_user']
    fields = ['tool_link', 'tag']
    search_fields = ['tool_link', 'tag']


# xadmin.site.register(Type, TypeAdminModel)
# xadmin.site.register(Tool,ToolAdminModel)