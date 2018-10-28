from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<id>', views.view_employee, name='view_employee'),
    path('edit/<pk>', views.EmployeeEditView.as_view(), name='edit_employee'),
    path('delete/<pk>', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('password/<pk>', views.employee_change_password, name='employee_change_password'),
    path('add', views.EmployeeCreateView.as_view(), name='add_employee'),
    path('groups/add', views.GroupCreateView.as_view(), name='add_group'),
    path('groups/view/<id>', views.view_group, name='view_group'),
    path('groups/edit/<pk>', views.GroupEditView.as_view(), name='edit_group'),
    path('groups/delete/<pk>', views.GroupDeleteView.as_view(), name='delete_group'),
]
