from django.db import models


class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME')
    mpg = models.FloatField(db_column='MPG')
    cyl = models.IntegerField(db_column='CYL')
    disp = models.FloatField(db_column='DISP')
    hp = models.IntegerField(db_column='HP')
    wt = models.FloatField(db_column='WT')
    qsec = models.FloatField(db_column='QSEC')
    vs = models.IntegerField(db_column='VS')
    am = models.IntegerField(db_column='AM')
    gear = models.IntegerField(db_column='GEAR')

    class Meta:
        managed = True
        db_table = 'MTCars'
        ordering = ['id']

    def __str__(self):
        '''
        Retorna a representação em string do objeto MTCars.
        Por exemplo, o que vai ser listado na
        interface de admin.
        '''
        return "Modelo: " + self.name
