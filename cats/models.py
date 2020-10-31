from django.db import models
from django.core.validators import MinLengthValidator


validate_fail_info = 'Must be longer than 2 characters'

class Breed(models.Model):

    name = models.CharField(max_length=200,
                            validators=[MinLengthValidator(2, validate_fail_info)])

    def __str__(self):

        return self.name


class Cat(models.Model):

    nickname = models.CharField(max_length=200,
                                validators=[MinLengthValidator(2, validate_fail_info)])
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):

        return self.nickname