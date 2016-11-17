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

class Prestamo(models.Model):
    id= models.AutoField(primary_key=True)
    fecha_entrega= models.DateTimeField(blank=True, null=True, default= None)
    fecha_devolucion= models.DateTimeField(blank=True, null=True, default= None)
    unidad=models.ForeignKey('Producto', null=False,blank=False, on_delete=models.CASCADE)


class Asignatura(models.Model):   
    id =models.AutoField(primary_key= True)
    Nombre= models.CharField(blank=False, null=False, max_length=100)
    año=models.DateField(blank=False, null=False,auto_now=False)
    MEstudiante = models.ForeignKey('Estudiante', null=False)

class Docente(models.Model):
    ocupacion= models.CharField(null=False,max_length=100,blank =False)
    titulo= models.CharField(null=False,max_length=100,blank =False)

class Pannolero(models.Model):
    info= models.ForeignKey('Docente',blank=False,null=False)
