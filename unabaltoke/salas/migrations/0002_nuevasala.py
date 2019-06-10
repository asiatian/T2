# Generated by Django 2.2.1 on 2019-06-07 06:14

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NuevaSala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('hora_inicio', models.IntegerField()),
                ('hora_cierre', models.IntegerField()),
                ('descripcion', models.CharField(max_length=300)),
            ],
            managers=[
                ('nueva', django.db.models.manager.Manager()),
            ],
        ),
    ]
