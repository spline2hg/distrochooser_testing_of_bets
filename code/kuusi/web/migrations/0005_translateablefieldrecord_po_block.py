# Generated by Django 4.2.4 on 2023-08-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0004_translateable_remove_choosable_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="translateablefieldrecord",
            name="po_block",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
