from django.db import models

# Create your models here.
class WeightData(models.Model):
    check_date = models.DateField()
    weight_value = models.FloatField()
    
    def __str__(self):
        return str(self.check_date) + ": " + str(self.weight_value)
   
