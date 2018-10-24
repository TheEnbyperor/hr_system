from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash


@permission_required("auth.view_user")
@permission_required("auth.view_group")
def index(request):
    employees = User.objects.all()
    return render(request, 'employees/index.html', {"employees": employees})


@permission_required("auth.view_user")
def view_employee(request, id):
    employee = get_object_or_404(User, id=id)
    return render(request, 'employees/view_employee.html', {"employee": employee})


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = User
    fields = ('username', 'password', 'first_name', 'last_name', 'is_superuser', 'groups', 'user_permissions',)
    permission_required = ('auth.add_user', )
    success_url = reverse_lazy('employees:index')
    template_name = "employees/employee_form.html"

    def form_valid(self, form):
        super().form_valid(form)
        password = self.object.password
        self.object.set_password(password)
        self.object.save()


class EmployeeEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'password', 'is_active', 'is_superuser', 'groups', 'user_permissions',
              'last_login', 'date_joined',)
    success_url = reverse_lazy('employees:index')
    permission_required = ('auth.change_user', )
    template_name = "employees/employee_update_form.html"

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.password = ""
        return object

    def form_valid(self, form):
        password = form.cleaned_data['password']
        self.object.set_password(password)
        self.object.save()
        form.cleaned_data['password'] = self.object.password
        return super().form_valid(form)


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('employees:index')
    permission_required = ('auth.delete_user', )
    template_name = "employees/employee_confirm_delete.html"
