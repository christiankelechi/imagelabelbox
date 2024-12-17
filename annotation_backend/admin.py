from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Annotation)
admin.site.register(models.AnnotationImage)
admin.site.register(models.AnnotationProject)