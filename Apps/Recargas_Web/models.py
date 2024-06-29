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
    identifier = models.IntegerField()
    local = models.CharField(max_length=100)
    registro = models.DateTimeField()
    tipo = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)
    bono = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=20)
    web_id = models.IntegerField()
    cliente = models.CharField(max_length=255)
    recarga = models.IntegerField()
    bono_5_por_ciento = models.IntegerField()
    promotor = models.CharField(max_length=100)

    class Meta:
        db_table = "GESTION_RW"  # Nombre de la tabla en la base de datos

    def registro_formateado(self):
        return self.Registro.strftime('%Y-%m-%d %H:%M:%S')
