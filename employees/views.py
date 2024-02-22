from django.shortcuts import render
from .models import Employee, Attendance
# xodimlar uchun view

def staff_create(request):
    """ xodimlarni familya ismini yaratish uchun """
    i_name = Employee.objects.POST['i_name']
    f_name = Employee.objects.POST['F_name']
    employes = Employee.objects.create(
        i_name=i_name,
        f_name=f_name
    )

    context = {
        'employes':employes
    }

    return render(request, context)


def staff_list(request):
    """ xodimlarni royhati """
    employe = Employee.objects.all()
    context = {
        'employe':employe
    }

    return render(request, context)


# davomat uchun view


def attendance_create(request):
    """ xodimlarni kelgan vaqtini yozib olish """
    time = Attendance.objects.POST['time']
    create = Attendance.objects.create(
        time=time,
    )
    context = {
        'create':create
    }
    return render(request, context)

def attendance_day(request):
    """ xodimlarni birkunlik davomati """
    ...

def attendance_week(request):
    """ xodimlarni bir haftalik davomati """
    ...

def attendance_month(request):
    """ xodimlarni bir oylik davomati"""
    ...


