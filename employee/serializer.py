from rest_framework import  serializers
from .models import Employees
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class EmployeeSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False)
    
    class Meta:
        model = Employees
        fields = ('emp_name','emp_mobile','emp_email','created_by','created_at')
