from django.contrib import admin

from mutant import models
from mutant.contrib.text import models as text_models
from mutant.contrib.numeric import models as numeric_models


admin.site.register(models.BaseDefinition)
admin.site.register(models.FieldDefinition)
admin.site.register(models.FieldDefinitionChoice)
admin.site.register(models.ModelDefinition)
admin.site.register(models.OrderingFieldDefinition)
admin.site.register(models.UniqueTogetherDefinition)

admin.site.register(text_models.CharFieldDefinition)
admin.site.register(numeric_models.IntegerFieldDefinition)
