from django.db import models
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=8)
    position = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} - {self.position}"

class Project(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 related_name='projects')
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True )
    def __str__(self):
        return self.name