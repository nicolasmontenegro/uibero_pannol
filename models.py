from django.db import models
from django.contrib.auth.models import User

class InfoProducto(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.PositiveIntegerField(blank=False, null=False, default=0)
    nombre = models.CharField(blank=False, null=False, max_length=100)
    marca = models.CharField(blank=True, null=False, max_length=100, default="OEM")
    modelo = models.CharField(blank=True, null=True, max_length=100)


    def __str__(self):
        return self.nombre
        

class Estudiante(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    SEMESTRES = (
        ('1', "Primero"),
        ('2', "Segundo"),
        ('3', "Tercero"),
        ('4', "Cuarto"),
        ('5', "Quinto"),
        ('6', "Sexto"),
        ('7', "Septimo"),
        ('8', "Octavo"),
        ('9', "Noveno"),
        ('10', "Decimo"),
    )
    MODALIDADES = (
        ('D', "Diurno"),
        ('V', "Vespertino"),
        ('T', "Tesista"),
    )
    
    carrera = models.CharField(blank=False, null=False, max_length=100)
    semestre = models.CharField(null=False, max_length=1, choices = SEMESTRES)
    modalidad = models.CharField(null=False, max_length=1, choices = MODALIDADES)

    def __unicode__(self):
        return self.user.first_name

class Producto(models.Model):
    ESTADOS = (
        ('0', "Funcional"),
        ('1', "Defectuoso"),
        ('2', "En reparación"),
        ('3', "Ausente"),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(null=False, max_length=1, choices = ESTADOS, default='0')
    serial = models.CharField(blank=True, max_length=100)
    informacion = models.ForeignKey('InfoProducto', null=True, on_delete=models.SET_NULL)

class asignatura(models.Model):
   
   id =models.AutoField(primary_key= True)
   Nombre= models.CharField(blanck=False, null=False, max_lenght=100)
   año=models.DateField(blanck=False, null=False,auto_now=False)
