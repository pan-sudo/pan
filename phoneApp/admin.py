from django.contrib import admin
from phoneApp import models

admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.Product)
admin.site.register(models.PPhoto)

# Register your models here.
