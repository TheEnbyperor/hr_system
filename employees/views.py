from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import models


def index(request):
    employees = models.Employee.objects.all()
    return render(request, 'employees/index.html', {"employees": employees})


def view_employee(request, id):
    employee = get_object_or_404(models.Employee, id=id)
    return render(request, 'employees/view_employee.html', {"employee": employee})


class EmployeeCreateView(CreateView):
    model = models.Employee
    fields = ('name',)
    success_url = reverse_lazy('employees:index')


class EmployeeEditView(UpdateView):
    model = models.Employee
    fields = ('name',)
    success_url = reverse_lazy('employees:index')
    template_name_suffix = "_update_form"


class EmployeeDeleteView(DeleteView):
    model = models.Employee
    success_url = reverse_lazy('employees:index')
