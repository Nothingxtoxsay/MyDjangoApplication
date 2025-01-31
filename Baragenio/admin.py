from django.contrib import admin
from .models import Owner, Pet, Vaccination, PetIncident, License

admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Vaccination)
admin.site.register(PetIncident)
admin.site.register(License)