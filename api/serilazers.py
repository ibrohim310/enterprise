from rest_framework import serializers
from employees import models

class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class ListEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class CreateAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class DayAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class WeekAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class MonthAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'