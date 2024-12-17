# Generated by Django 4.2.4 on 2024-12-17 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("annotation_backend", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="annotation",
            name="height",
        ),
        migrations.RemoveField(
            model_name="annotation",
            name="width",
        ),
        migrations.RemoveField(
            model_name="annotation",
            name="x",
        ),
        migrations.RemoveField(
            model_name="annotation",
            name="y",
        ),
        migrations.AddField(
            model_name="annotation",
            name="image_label",
            field=models.TextField(blank=True, null=True),
        ),
    ]