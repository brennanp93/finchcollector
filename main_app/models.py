from django.db import models
from django.urls import reverse

TIMEOFDAY = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening')
)


# Create your models here.

class Seed(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('seeds_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    common_name = models.CharField(max_length=100)
    migratory = models.BooleanField(default=True)
    range = models.CharField(max_length=100)
    seeds = models.ManyToManyField(Seed)


 # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
    def __str__(self):
        return f'{self.common_name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Sighting(models.Model):
    date = models.DateField('Date of Sighting')
    time = models.CharField(
        max_length=1,
        choices=TIMEOFDAY,
        default=TIMEOFDAY[0][0]
    )

    # create a finch_id FK
    finch = models.ForeignKey(
        Finch, 
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']