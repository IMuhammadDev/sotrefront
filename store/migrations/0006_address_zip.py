# Generated by Django 4.2.3 on 2023-08-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_alter_produckt_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="zip",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
