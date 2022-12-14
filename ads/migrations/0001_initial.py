# Generated by Django 4.1.4 on 2022-12-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ads",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("author", models.CharField(max_length=20)),
                ("price", models.IntegerField()),
                ("description", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                (
                    "is_published",
                    models.CharField(
                        choices=[(True, "TRUE"), (False, "FALSE")],
                        default="True",
                        max_length=5,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Categories",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
