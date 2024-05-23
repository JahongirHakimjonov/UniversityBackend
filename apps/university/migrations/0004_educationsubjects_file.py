# Generated by Django 5.0.3 on 2024-05-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("university", "0003_educationsubjectscategory_educationsubjects"),
    ]

    operations = [
        migrations.AddField(
            model_name="educationsubjects",
            name="file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="education_subjects/",
                verbose_name="File",
            ),
        ),
    ]