# Generated by Django 4.2.4 on 2023-09-04 09:09

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contributor",
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
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=128, unique=True)),
                ("description", models.TextField(blank=True, max_length=2048)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("BE", "Backend"),
                            ("FE", "Frontend"),
                            ("i", "iOS"),
                            ("A", "Android"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "contributors",
                    models.ManyToManyField(
                        related_name="projects",
                        through="issues.Contributor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Issue",
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
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True, max_length=2048)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("TODO", "To Do"),
                            ("PROG", "In Progress"),
                            ("FINI", "Finished"),
                        ],
                        default="TODO",
                        max_length=4,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[("L", "LOW"), ("M", "MEDIUM"), ("H", "HIGH")],
                        max_length=1,
                    ),
                ),
                (
                    "tag",
                    models.CharField(
                        choices=[("BUG", "Bug"), ("TASK", "Task"), ("FEAT", "Feature")],
                        max_length=4,
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="issues_assigned",
                        to="issues.contributor",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues",
                        to="issues.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="contributor",
            name="contribute_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="issues.project"
            ),
        ),
        migrations.AddField(
            model_name="contributor",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contributions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField(max_length=2048)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="issues.issue",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterUniqueTogether(
            name="contributor",
            unique_together={("user", "contribute_to")},
        ),
    ]
