# Generated by Django 4.1.4 on 2022-12-17 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_rename_location_id_user_location"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["username"],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
