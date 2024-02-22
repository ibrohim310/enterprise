from django.db import models


class Employee(models.Model):
    """ korxona uchun mijozlar modeli """
    f_name = models.CharField(max_length=255)
    i_name = models.CharField(max_length=255)


class Attendance(models.Model):
    """ korxonada mijozlarni davomatini belgilash uchun model """
    time = models.DateTimeField()

    
