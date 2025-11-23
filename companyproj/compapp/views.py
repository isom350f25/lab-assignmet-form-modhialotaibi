from django.shortcuts import render, redirect
from .models import Employee, Project
from django.utils import timezone
from .forms import EmployeeForm, ProjectForm
# Create your views here.
def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})
def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    today = timezone.now().date()
    projects = employee.projects.filter(start_date__lte=today,
                                        end_date__gte=today  )
    #projects = employee.projects.all()
    return render(request, 'employee_detail.html',
                  {'employee': employee, 'projects': projects})
def employee_engineers(request):
    employees = Employee.objects.filter(position__icontains="engineer")
    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
   if request.method == 'POST':
       form = EmployeeForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('employee_list')
   else:
       form = EmployeeForm()        
   return render(request, 'add_employee.html', {'form': form})

def add_project(request):
   if request.method == 'POST':
       form = ProjectForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('employee_list')
   else:
       form = ProjectForm()          
   return render(request, 'add_project.html', {'form': form})