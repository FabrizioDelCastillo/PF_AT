# Generated by Django 5.0.6 on 2024-06-15 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recargas_Web', '0003_rename_fecha_modificacion_calimaco_fecha_de_modificacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calimaco',
            old_name='Fecha_registro_jugador',
            new_name='Fecha_de_registro_del_jugador',
        ),
    ]