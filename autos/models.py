from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Auto(models.Model):

    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Must be greater than one character")])
    mileage = models.PositiveIntegerField()
    comments = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Must be greater than one character")])
    make = models.ForeignKey('make', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.nickname

class Make(models.Model):

    name = models.CharField(
        max_length=200,
        help_text='Please enter a make name (e.g. Toyota)',
        validators=[MinLengthValidator(2, "Must be greater than one character")])

    def __str__(self):
        return self.name