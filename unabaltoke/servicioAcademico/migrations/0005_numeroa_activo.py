# Generated by Django 2.2.1 on 2019-06-21 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicioAcademico', '0004_auto_20190620_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='numeroa',
            name='activo',
            field=models.BinaryField(default=True),
        ),
    ]