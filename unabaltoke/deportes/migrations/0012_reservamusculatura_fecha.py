# Generated by Django 2.2.1 on 2019-06-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0011_auto_20190609_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservamusculatura',
            name='Fecha',
            field=models.DateField(null=True),
        ),
    ]
