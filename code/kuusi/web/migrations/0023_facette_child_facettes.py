# Generated by Django 4.2.4 on 2023-08-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0022_facette_topic"),
    ]

    operations = [
        migrations.AddField(
            model_name="facette",
            name="child_facettes",
            field=models.ManyToManyField(to="web.facette"),
        ),
    ]
