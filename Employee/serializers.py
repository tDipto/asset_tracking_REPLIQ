from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["company","phone","address"]

class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = User
        fields = ['id', 'username',"first_name", "email", 'password','employee']
        extra_kwargs = {'password':{"write_only":True, 'required':True}}

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        user = User.objects.create_user(**validated_data)
        user.employee = Employee.objects.create(user=user, **employee_data)
        user.save()
        return user

   