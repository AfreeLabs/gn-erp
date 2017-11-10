from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from apps.departement.models import Department
from apps.school.models import AcademicYear

class Registration(models.Model):
    GENDER_CHOICE = (
        ('homme', 'homme'),
        ('femme', 'femme'),
    )

    OPTION_CHOICE = (
        ('sm', 'Sciences Mathématiques'),
        ('se', 'Sciences Experimentales'),
        ('ss', 'Sciences Sociales'),
    )

    registry_number = models.CharField(max_length=15, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    date_of_birth = models.DateField()
    nationality = CountryField()
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True)
    id_card_number = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_email = models.EmailField(max_length=100, blank=True, null=True)
    guardian_address = models.CharField(max_length=100, blank=True, null=True)
    school_origin = models.CharField(max_length=100, blank=True, null=True)
    option = models.CharField(max_length=2, choices=OPTION_CHOICE)
    year_admission_bac = models.CharField(max_length=4, blank=True, null=True)
    pv = models.CharField(max_length=10, blank=True, null=True)
    registration_add_date = models.DateTimeField(auto_now_add=True)
    registration_modify_date = models.DateTimeField(auto_now=True)
    student_card = models.CharField(max_length=200, editable=False)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='registrations')
    


    class Meta:
        unique_together = ('email', 'student_card')

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Admission(models.Model):
    registry = models.OneToOneField(Registration, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='registrations')
    fees = models.IntegerField()
    matricule = models.CharField(max_length=15, editable=False)
    admission_add_date = models.DateTimeField(auto_now_add=True)
    admission_modify_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return '{0}'.format(self.registry)


@receiver(pre_save, sender=Registration)
def generate_student_card(sender, instance, *args, **kwargs):
    prefix = 'OR/2017/00000'
    if Registration.objects.last():
        instance.registry_number = prefix + str(Registration.objects.last().id + 1)
    else:
        instance.registry_number = prefix + '1'

@receiver(pre_save, sender=Admission)
def generate_student_matricule(sender, instance, *args, **kwargs):
    prefix = 'MAT/2017/00000'
    if Admission.objects.last():
        instance.matricule = prefix + str(Admission.objects.last().id + 1)
    else:
        instance.matricule = prefix + '1'
