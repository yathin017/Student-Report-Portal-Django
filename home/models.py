from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Student(models.Model):
    name=               models.CharField(max_length=150, default=None)
    roll_number=        models.IntegerField(unique=True)
    email=              models.EmailField(max_length=150, default=None)
    branch=             models.CharField(max_length=10, default=None)
    ITW_marks_1=        models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    ITW_marks_2=        models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    ITW_marks_3=        models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    IoT_marks_1=        models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    IoT_marks_2=        models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    IoT_marks_3=        models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    Stats_marks_1=      models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    Stats_marks_2=      models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    Stats_marks_3=      models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    Clang_marks_1=      models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    Clang_marks_2=      models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    Clang_marks_3=      models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    ITW_attendance=     models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    IoT_attendance=     models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    Stats_attendance=   models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    Clang_attendance=   models.PositiveIntegerField(validators=[MaxValueValidator(101)], default=None)
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    prob=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name