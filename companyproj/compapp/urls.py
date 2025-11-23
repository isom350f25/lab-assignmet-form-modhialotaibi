from django.urls import path
from . import views


urlpatterns = [
    path('employeeslist/', views.employee_list, name='employee_list'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('engineers/', views.employee_engineers, name='employee_engineers'),
    path('add/employee/', views.add_employee, name='add_employee'),
    path('add/project/', views.add_project, name='add_project'),
]