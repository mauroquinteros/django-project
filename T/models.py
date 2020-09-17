from django.db import models

# Create your models here.
class Empleado(models.Model):
  codPers = models.IntegerField(primary_key=True, )
  direcc = models.CharField(max_length=100, blank=False)
  hobby = models.TextField(blank=False)
  fecNac = models.DateField()
  dni = models.CharField(max_length=20, blank=False)
  nroCIP = models.CharField(max_length=10)
  fecCIPVig = models.DateField()
  licCond = models.CharField(max_length=1)
  observac = models.CharField(max_length=300)
  vigente = models.CharField(max_length=1)

  def __str__(self):
    return self.dni


class Proyecto(models.Model):
  codPyto = models.IntegerField(primary_key=True)
  codSNIP = models.CharField(max_length=10)
  fecReg = models.DateField()
  codFase = models.IntegerField()
  codNivel = models.IntegerField()
  codFuncion = models.CharField(max_length=4)
  codSituacion = models.IntegerField()
  numInfor = models.IntegerField()
  numInforEntrg = models.IntegerField()
  estPyto = models.IntegerField()
  fecEstado = models.DateField()
  nomPyto = models.TextField()
  emplJefeProj = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  valRefer = models.DecimalField(max_digits=6, decimal_places=2)
  costoTotal = models.DecimalField(max_digits=6, decimal_places=2)
  costDirecto = models.DecimalField(max_digits=6, decimal_places=2)
  costGGen = models.DecimalField(max_digits=6, decimal_places=2)
  costImp = models.CharField(max_length=100)
  costPenalid = models.CharField(max_length=100)
  codDpto = models.CharField(max_length=2)
  codProv = models.CharField(max_length=2)
  codDist = models.CharField(max_length=2)
  fechViab = models.DateField()
  observac = models.CharField(max_length=500)
  rutaDoc = models.CharField(max_length=300)
  codObjc = models.IntegerField()
  vigente = models.CharField(max_length=1)
  codPersona = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.nomPyto


class Ruta(models.Model):
  codPyto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
  codRutaPy = models.IntegerField(primary_key=True)
  nroVersion = models.IntegerField()
  codRuta = models.CharField(max_length=20)
  fechaRegistro = models.DateField()
  denominacionRuta = models.CharField(max_length=100)
  denominacionCortoRuta = models.CharField(max_length=100)
  nroKms = models.DecimalField(max_digits=6, decimal_places=2)
  zonaGPS = models.CharField(max_length=25)
  progInicio = models.CharField(max_length=25)
  progFinal = models.CharField(max_length=25)
  latitudInicioRuta = models.CharField(max_length=25)
  latitudFinalRuta = models.CharField(max_length=25)
  longitudInicioRuta = models.CharField(max_length=25)
  longitudFinalRuta = models.CharField(max_length=25)
  altitudInicioRuta = models.CharField(max_length=25)
  altitudFinalRuta = models.CharField(max_length=25)
  observacionRuta = models.CharField(max_length=500)
  vigencia = models.CharField(max_length=1)
  elaboradorPor = models.ForeignKey(Empleado, on_delete=models.CASCADE)


class Tramo(models.Model):
  codRutaPy = models.ForeignKey(Ruta, on_delete=models.CASCADE)
  codTramoPy = models.IntegerField(primary_key=True)
  nroVersion = models.IntegerField()
  codTramo = models.CharField(max_length=20)
  fechaRegistro = models.DateField()
  denominacionTramo = models.CharField(max_length=100)
  denominacionCortoTramo = models.CharField(max_length=100)
  nroKmsTramo = models.DecimalField(max_digits=6, decimal_places=2)
  zonaGPS = models.CharField(max_length=25)
  progInicio = models.CharField(max_length=25)
  progFin = models.CharField(max_length=25)
  latitudInicioTramo = models.CharField(max_length=25)
  latitudFinalTramo = models.CharField(max_length=25)
  longitudInicioTramo = models.CharField(max_length=25)
  longitudFinalTramo = models.CharField(max_length=25)
  altitudInicioTramo = models.CharField(max_length=25)
  altitudFinalTramo = models.CharField(max_length=25)
  observacionTramo = models.CharField(max_length=500)
  vigencia = models.CharField(max_length=1)