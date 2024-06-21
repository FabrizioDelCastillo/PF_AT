# Importa los modelos de Django
from django.db import models

# Modelo para la tabla CALIMACO
class Calimaco(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    Cliente = models.IntegerField(default=0)
    Fecha = models.DateTimeField()
    Estado = models.CharField(max_length=100)
    Fecha_de_modificacion = models.DateTimeField()
    Usuario = models.CharField(max_length=100)
    Email = models.EmailField()
    Cantidad = models.IntegerField(default=0)
    Id_externo = models.IntegerField()
    Respuesta = models.CharField(max_length=255)
    Agente = models.IntegerField()
    Fecha_de_registro_del_jugador = models.DateTimeField()

    class Meta:
        db_table = 'CALIMACO'  # Nombre de la tabla en la base de datos

# Modelo para la tabla GESTION_RW
class GestionRW(models.Model):
    Identifier = models.IntegerField()
    Local = models.CharField(max_length=100)
    Registro = models.DateTimeField()
    Tipo = models.CharField(max_length=100)
    Proveedor = models.CharField(max_length=100)
    Bono = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=20)
    Tipo_documento = models.CharField(max_length=10)
    Numero_documento = models.CharField(max_length=20)
    Web_id = models.IntegerField()
    Cliente = models.CharField(max_length=255)
    Recarga = models.IntegerField()
    Bono_5_por_ciento = models.IntegerField()
    Promotor = models.CharField(max_length=100)

    class Meta:
        db_table = 'GESTION_RW'  # Nombre de la tabla en la base de datos
