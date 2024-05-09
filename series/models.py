from django.db import models

class Serie(models.Model):

    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Fecha de registro')
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    detalle = models.TextField(max_length=1000, null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Fecha de registro')
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre