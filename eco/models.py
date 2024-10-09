from django.db import models

# Create your models here.
class Plant(models.Model):
    plant_name=models.TextField(max_length=100)
    scientific_name=models.TextField(max_length=100)
    price=models.IntegerField(default=100)
    age=models.IntegerField()
    pic=models.ImageField(null=True)
    imported=models.BooleanField(default=False)
    imported = models.BooleanField(default=False)

    def __str__(self) ->str:
        return self.plant_name
