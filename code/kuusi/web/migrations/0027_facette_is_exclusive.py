# Generated by Django 4.2.4 on 2023-08-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0026_alter_facette_child_facettes"),
    ]

    operations = [
        migrations.AddField(
            model_name="facette",
            name="is_exclusive",
            field=models.BooleanField(default=False),
        ),
    ]
