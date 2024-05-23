# Generated by Django 5.0.3 on 2024-05-23 08:47

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("university", "0004_educationsubjects_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="AcademicHours",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "short_title",
                    models.CharField(max_length=255, verbose_name="Short Title"),
                ),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
                ),
                (
                    "short_description",
                    models.TextField(verbose_name="Short Description"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="academic_hours/", verbose_name="Image"
                    ),
                ),
            ],
            options={
                "verbose_name": "Academic Hours",
                "verbose_name_plural": "Academic Hours",
                "db_table": "academic_hours",
            },
        ),
        migrations.CreateModel(
            name="EducationServices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "short_title",
                    models.CharField(max_length=255, verbose_name="Short Title"),
                ),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
                ),
                (
                    "short_description",
                    models.TextField(verbose_name="Short Description"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="education_services/", verbose_name="Image"
                    ),
                ),
            ],
            options={
                "verbose_name": "Education Services",
                "verbose_name_plural": "Education Services",
                "db_table": "education_services",
            },
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "short_title",
                    models.CharField(max_length=255, verbose_name="Short Title"),
                ),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
                ),
                (
                    "short_description",
                    models.TextField(verbose_name="Short Description"),
                ),
                ("image", models.ImageField(upload_to="news/", verbose_name="Image")),
            ],
            options={
                "verbose_name": "News",
                "verbose_name_plural": "News",
                "db_table": "news",
            },
        ),
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "short_title",
                    models.CharField(max_length=255, verbose_name="Short Title"),
                ),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
                ),
                (
                    "short_description",
                    models.TextField(verbose_name="Short Description"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="projects/", verbose_name="Image"),
                ),
            ],
            options={
                "verbose_name": "Projects",
                "verbose_name_plural": "Projects",
                "db_table": "projects",
            },
        ),
        migrations.CreateModel(
            name="ScientificBase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "short_title",
                    models.CharField(max_length=255, verbose_name="Short Title"),
                ),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
                ),
                (
                    "short_description",
                    models.TextField(verbose_name="Short Description"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="scientific_base/", verbose_name="Image"
                    ),
                ),
            ],
            options={
                "verbose_name": "Scientific Base",
                "verbose_name_plural": "Scientific Base",
                "db_table": "scientific_base",
            },
        ),
    ]