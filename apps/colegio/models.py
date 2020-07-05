from django.db import models

class Institucion(models.Model):
    id_institucion = models.AutoField(primary_key = True)
    institucion = models.CharField(max_length = 200, blank = False, null = True)
        
    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'
    
    def __str__(self):
        return self.institucion

class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key = True)
    rut = models.CharField(max_length = 200, blank = False, null = False)
    nombre_completo = models.CharField(max_length = 200, blank = False, null = False)
    email = models.EmailField(max_length = 200, blank = False, null = False)
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
    
    def __str__(self):
        return self.nombre_completo

class Seguro(models.Model):
    id = models.CharField(max_length = 200, primary_key = True)
    adjunto_seguro = models.FileField(blank = True, null = True)
    
    class Meta:
        verbose_name = 'Seguro'
        verbose_name_plural = 'Seguros'
    
    def __str__(self):
        return self.id

class Apoderado(models.Model):
    rut = models.CharField(max_length = 200, primary_key = True)
    nombre_completo = models.CharField(max_length = 200, blank = False, null = False)
    email = models.EmailField(max_length = 200, blank = False, null = False)
    
    class Meta:
        verbose_name = 'Apoderado'
        verbose_name_plural = 'Apoderados'
    
    def __str__(self):
        return self.nombre_completo

class Contrato(models.Model):
    id_contrato = models.CharField(max_length = 200, primary_key = True)
    vendedor_id = models.ForeignKey(Vendedor, default = '', on_delete = models.CASCADE)
    fecha_contrato = models.DateField(blank =  False, null =  False)
    fecha_viaje = models.DateField(blank =  False, null =  False)
    nombre_completo_apoderado = models.OneToOneField(Apoderado, on_delete = models.CASCADE)
    nro_alumnos = models.IntegerField(blank = True, null = False)
    adjunto_contrato = models.FileField(blank = True, null = True)
    institucion_id = models.OneToOneField(Institucion, on_delete = models.CASCADE)
    seguro_id = models.OneToOneField(Seguro, default = '', on_delete = models.CASCADE)
    monto = models.IntegerField(blank = True, null = False)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return self.id_contrato
        


