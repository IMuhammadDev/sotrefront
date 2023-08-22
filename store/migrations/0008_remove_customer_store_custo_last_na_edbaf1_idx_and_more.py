# Generated by Django 4.2.3 on 2023-08-20 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_customer_store_custo_last_na_edbaf1_idx_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="customer",
            name="store custo_last_na_edbaf1_idx",
        ),
        migrations.RenameField(
            model_name="customer",
            old_name="first_name",
            new_name="given_name",
        ),
        migrations.AlterModelTable(
            name="customer",
            table=None,
        ),
    ]
