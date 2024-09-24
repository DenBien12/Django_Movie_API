from django.db import models

# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.last_name},{self.first_name}'
    

class Gerne(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Movies(models.Model):
    name = models.CharField(max_length=250)
    director = models.ForeignKey('Director', on_delete=models.RESTRICT)
    gerne = models.ManyToManyField(Gerne)
    summary = models.TextField(max_length=1000)
    released_date = models.DateField(null=True, blank=True)
    def __str__(self) -> str:
        return self.name
    
    