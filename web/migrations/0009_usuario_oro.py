# Generated by Django 5.1.2 on 2024-10-31 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_tripulacion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='oro',
            field=models.IntegerField(default=100),
        ),
    ]