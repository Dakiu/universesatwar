# Generated by Django 5.1.2 on 2024-11-02 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_nave_resistencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nave',
            name='resistencia',
        ),
        migrations.AddField(
            model_name='tripulacion_usuario',
            name='resistencia',
            field=models.IntegerField(default=0),
        ),
    ]
