from django.db import models

# Create your models here.
    

class Movies(models.Model):
    name = models.CharField(max_length=250)
    director = models.CharField(max_length=100)
    released_date = models.DateField(null=True, blank=True)
    def __str__(self) -> str:
        return self.name
    
    