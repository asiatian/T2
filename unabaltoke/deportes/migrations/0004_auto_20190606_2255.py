# Generated by Django 2.2.1 on 2019-06-07 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0003_reservamusculatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservamusculatura',
            name='dia',
            field=models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado')]),
        ),
    ]
