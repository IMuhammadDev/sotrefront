# Generated by Django 4.2.4 on 2023-09-03 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_customer_store_custo_last_na_edbaf1_idx_and_more'),
    ]

    operations = [
        migrations.RunSQL("""
                INSERT INTO store_collection (title)
                VALUES ('collection1')
             ""","""
                DELETE FROM store_collection
                WHERE title='collection1'
             """)
    ]
