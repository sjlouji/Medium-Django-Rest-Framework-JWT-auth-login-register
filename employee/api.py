from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employees

class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeApi(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
