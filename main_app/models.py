from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    common_name = models.CharField(max_length=100)
    migratory = models.BooleanField()
    range = models.CharField(max_length=100)


 # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
    def __str__(self):
        return f'{self.common_name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})