from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets")

    def __str__(self):
        return f"{self.name} ({self.species})"


class Vaccination(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="vaccinations")
    vaccine_name = models.CharField(max_length=100)
    vaccination_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.vaccine_name} for {self.pet.name}"


class PetIncident(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="incidents")
    incident_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Incident on {self.incident_date} involving {self.pet.name}"


class License(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="licenses")
    license_number = models.CharField(max_length=50, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"License {self.license_number} for {self.pet.name}"