# Generated by Django 4.2.3 on 2023-07-23 12:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0004_sharedfile_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SharedFile",
        ),
    ]