# Generated by Django 5.1.2 on 2024-11-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_tripulacion_radar'),
    ]

    operations = [
        migrations.AddField(
            model_name='nave_usuario',
            name='ataque',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nave_usuario',
            name='comunicaciones',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nave_usuario',
            name='defensa',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nave_usuario',
            name='escudos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nave_usuario',
            name='radar',
            field=models.IntegerField(default=0),
        ),
    ]
