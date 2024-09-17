from django.db import models

class Productor(models.Model):
    documento_identidad = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

class Finca(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    numero_catastro = models.IntegerField()
    municipio = models.CharField(max_length=100)

class Vivero(models.Model):
    codigo = models.IntegerField()
    tipo_cultivo = models.CharField(max_length=100)

class Labor(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()

class ProductoControl(models.Model):
    registro_ica = models.IntegerField()
    nombre_producto = models.CharField(max_length=100)
    frecuencia_aplicacion = models.IntegerField()
    valor_producto = models.DecimalField(max_digits=10, decimal_places=2)

class ProductoControlHongo(ProductoControl):
    nombre_hongo = models.CharField(max_length=100)
    periodo_carencia = models.IntegerField()

class ProductoControlPlaga(ProductoControl):
    periodo_carencia = models.IntegerField()

class ProductoControlFertilizante(ProductoControl):
    fecha_ultima_aplicacion = models.DateField()
      
