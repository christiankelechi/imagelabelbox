# Generated by Django 4.2.4 on 2024-12-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "annotation_backend",
            "0003_annotation_height_annotation_width_annotation_x_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="annotationimage",
            name="image",
            field=models.FileField(upload_to="images"),
        ),
    ]
