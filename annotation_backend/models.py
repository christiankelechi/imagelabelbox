from django.db import models

# Create your models here.
from django.db import models

class AnnotationProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class AnnotationImage(models.Model):
    project = models.ForeignKey(AnnotationProject, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for Project: {self.project.name} with id {self.id}"


class Annotation(models.Model):
    image = models.ForeignKey(AnnotationImage, on_delete=models.CASCADE, related_name='annotations')
    image_label=models.TextField(null=True,blank=True)

    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)

    def __str__(self):
        return f"added annotation for ID: {self.image.id}"
