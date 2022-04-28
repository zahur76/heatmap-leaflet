from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Accidents(models.Model):
    """
    A model to store accident data
    
    """
    class Meta:
        verbose_name_plural = "Accidents"
        
    region = models.CharField(max_length=254, null=True)
    location = models.PointField(null=True)
    accident_number = models.IntegerField(null=True)

    def __str__(self):
        return self.region