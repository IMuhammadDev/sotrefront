# Generated by Django 4.2.4 on 2023-09-03 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20230903_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produckt',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.collection'),
        ),
    ]
