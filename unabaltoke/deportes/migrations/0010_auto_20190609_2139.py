# Generated by Django 2.2.1 on 2019-06-10 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0009_auto_20190609_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tallerdeportivo',
            name='icono',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='icons/%Y/%m/%d/'),
        ),
    ]
