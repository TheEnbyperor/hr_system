from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<id>', views.view_employee, name='view_employee'),
    path('edit/<pk>', views.EmployeeEditView.as_view(), name='edit_employee'),
    path('delete/<pk>', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('add', views.EmployeeCreateView.as_view(), name='add_employee'),
]
