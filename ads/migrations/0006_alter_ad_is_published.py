# Generated by Django 4.1.4 on 2022-12-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0005_rename_author_id_ad_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="is_published",
            field=models.BooleanField(default=True),
        ),
    ]