from django.contrib import admin

from mutant import models


for field_type in models.FieldDefinitionBase._field_definitions.values():
    attrs = {'model': field_type}
    FieldDefAdmin = type('{0}Admin'.format(field_type.__name__),
                         (admin.ModelAdmin,),
                         attrs)
    admin.site.register(field_type, FieldDefAdmin)


class ModelDefinitionAdmin(admin.ModelAdmin):
    model = models.ModelDefinition


admin.site.register(models.ModelDefinition, ModelDefinitionAdmin)
