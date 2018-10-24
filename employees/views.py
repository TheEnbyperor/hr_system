from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm


@permission_required("auth.view_user")
@permission_required("auth.view_group")
def index(request):
    employees = User.objects.all()
    groups = Group.objects.all()
    return render(request, 'employees/index.html', {"employees": employees, "groups": groups})


@permission_required("auth.view_user")
def view_employee(request, id):
    employee = get_object_or_404(User, id=id)
    return render(request, 'employees/view_employee.html', {"employee": employee})


@permission_required("auth.view_group")
def view_group(request, id):
    group = get_object_or_404(Group, id=id)
    return render(request, 'employees/view_group.html', {"group": group})


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


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ('name', 'permissions',)
    permission_required = ('auth.add_group', )
    success_url = reverse_lazy('employees:index')
    template_name = "employees/group_form.html"


class EmployeeEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'is_active', 'is_superuser', 'groups', 'user_permissions',
              'last_login', 'date_joined',)
    success_url = reverse_lazy('employees:index')
    permission_required = ('auth.change_user', )
    template_name = "employees/employee_update_form.html"


class GroupEditView(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ('name', 'permissions',)
    success_url = reverse_lazy('employees:index')
    permission_required = ('auth.change_group', )
    template_name = "employees/group_update_form.html"


@permission_required("auth.change_user")
def employee_change_password(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AdminPasswordChangeForm(user)
    return render(request, 'employees/employee_change_password.html', {
        'form': form,
        'object': user,
    })


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('employees:index')
    permission_required = ('auth.delete_user', )
    template_name = "employees/employee_confirm_delete.html"


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('employees:index')
    permission_required = ('auth.delete_group', )
    template_name = "employees/group_confirm_delete.html"
