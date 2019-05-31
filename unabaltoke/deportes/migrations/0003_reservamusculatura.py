# Generated by Django 2.2.1 on 2019-05-31 02:39

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0002_auto_20190530_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaMusculatura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=14)),
                ('dia', models.IntegerField()),
                ('bloque', models.IntegerField()),
            ],
            managers=[
                ('reservas', django.db.models.manager.Manager()),
            ],
        ),
    ]
