# Generated by Django 5.0.6 on 2024-06-15 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recargas_Web', '0002_rename_agente_calimaco_agente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calimaco',
            old_name='Fecha_modificacion',
            new_name='Fecha_de_modificacion',
        ),
    ]