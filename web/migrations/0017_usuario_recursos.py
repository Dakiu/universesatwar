# Generated by Django 5.1.2 on 2024-11-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_nave_usuario_ataque_nave_usuario_comunicaciones_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='recursos',
            field=models.IntegerField(default=0),
        ),
    ]
