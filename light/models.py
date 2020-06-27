from django.db import models

class Participant(models.Model):
    sex_choice = [
        ('male', "male"),
        ('female', "female"),
    ]

    name = models.CharField(max_length=100)
    sex = models.CharField(choices=sex_choice, max_length=10)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    aadhar_no = models.IntegerField()
    phone_no = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name