# Generated by Django 5.0.6 on 2024-06-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recargas_Web', '0004_rename_fecha_registro_jugador_calimaco_fecha_de_registro_del_jugador'),
    ]

    operations = [
        migrations.AddField(
            model_name='calimaco',
            name='Cliente',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calimaco',
            name='Id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
