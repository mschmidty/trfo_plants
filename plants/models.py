from django.db import models
from django.urls import reverse

class Family(models.Model):
    family = models.CharField(max_length = 100)
    family_description = models.TextField(null = True)

    def get_absolute_url(self):
        return reverse('plants:family-detail', kwargs={'pk':self.pk})

    def __str__(self):
        family_name = "%s" %str(self.family)
        return(family_name)

# Create your models here.
class plant_basics(models.Model):
    genus = models.CharField(max_length = 500)
    species = models.CharField(max_length = 500)
    symbol = models.CharField(max_length = 6, null = True)
    common_name = models.CharField(max_length = 100, null = True)
    description = models.TextField(null = True)
    image = models.ImageField(upload_to='images/', blank = True, null = True)
    family = models.ForeignKey(Family, on_delete = models.PROTECT, null = True)

    def __str__(self):
        sci_name = "%s %s" %(str(self.genus), str(self.species))
        return(sci_name)

    def get_absolute_url(self):
        return reverse('plants:detail', kwargs={'pk':self.pk})


