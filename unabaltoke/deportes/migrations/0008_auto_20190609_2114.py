# Generated by Django 2.2.1 on 2019-06-10 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0007_auto_20190609_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tallerdeportivo',
            name='icono',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
