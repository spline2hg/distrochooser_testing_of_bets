# Generated by Django 4.2.4 on 2024-01-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0086_remove_choosablemeta_meta_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="referrer",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
