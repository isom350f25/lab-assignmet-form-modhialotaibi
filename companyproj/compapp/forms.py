from django import forms
from .models import Project , Employee


class Employee(forms.ModelForm):
    class Meta:
      model = Employee
      fields = ["name", "date_joined", "date_of_birth", "phone_number","position"]
      
      

class Project(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "start_date", "end_date", "amount"]
    