from django.contrib import admin
from .models import Finch, Sighting, Seed

# Register your models here.
admin.site.register(Finch)
admin.site.register(Sighting)
admin.site.register(Seed)