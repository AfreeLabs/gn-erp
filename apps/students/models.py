from django.db import models
from apps.admission.models import Registration

# Create your models here.

class Students(models.Model):
    registree = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name='registration_student')

    def __str__(self):
        return (self.registree.reg_inscription.matricule)


# class grades(models.Model):



# the payement of de students
class Payement(models.Model):
    registree = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='registration_payement')
    payment_type = models.CharField(max_length=64)
    date = models.DateField()
    amount = models.DecimalField(max_digits=32, decimal_places=2)

    def __str__(self):
        return '{0} {1}'.format(self.payment_type, self.registree.first_name)

