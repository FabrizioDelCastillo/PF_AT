# Importa los modelos de Django
from django.db import models

class Calimaco(models.Model):
    cliente = models.CharField(max_length=20, default="Unknown")
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20, default="Pending")
    fecha_modificacion = models.DateTimeField()
    usuario = models.CharField(max_length=20, default="Unknown")
    email = models.EmailField(default="example@example.com")
    cantidad = models.IntegerField(default=0)
    id_externo = models.CharField(max_length=20, default="Unknown")
    respuesta = models.TextField(default="N/A")
    agente = models.IntegerField(default=0)
    fecha_de_registro_del_jugador = models.DateTimeField()

    class Meta:
        db_table = "CALIMACO"  # Nombre de la tabla en la base de datos

    def fecha_formateada(self):
        return self.fecha.strftime('%Y-%m-%d %H:%M:%S')

    def fecha_modificacion_formateada(self):
        return self.fecha_modificacion.strftime('%Y-%m-%d %H:%M:%S')

    def fecha_de_registro_formateada(self):
        return self.fecha_de_registro_del_jugador.strftime('%Y-%m-%d %H:%M:%S')


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
        db_table = "GESTION_RW"  # Nombre de la tabla en la base de datos

    def registro_formateado(self):
        return self.Registro.strftime('%Y-%m-%d %H:%M:%S')
