from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Sum

from .models import Employee
from .forms import EmployeeForm


@login_required
def employee_list(request):
    employees = Employee.objects.all()

    department_data = (
        Employee.objects
        .values('department')
        .annotate(total=Count('id'))
        .order_by('department')
    )

    department_labels = [
        item['department'] or 'Unassigned'
        for item in department_data
    ]
    department_counts = [item['total'] for item in department_data]

    return render(request, 'studentapp/employee_list.html', {
        'employees': employees,
        'department_labels': department_labels,
        'department_counts': department_counts,
    })


@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'studentapp/employee_form.html', {'form': form})


@login_required
def reports(request):
    total_employees = Employee.objects.count()

    department_data = (
        Employee.objects
        .values('department')
        .annotate(total=Count('id'))
        .order_by('department')
    )

    average_salary = Employee.objects.aggregate(
        average=Avg('salary')
    )['average'] or 0

    total_salary = Employee.objects.aggregate(
        total=Sum('salary')
    )['total'] or 0

    return render(request, 'studentapp/reports.html', {
        'total_employees': total_employees,
        'department_data': department_data,
        'average_salary': average_salary,
        'total_salary': total_salary,
    })