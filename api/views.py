from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from .models import Student
from .serializers import StudentSerializer


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ['name']
    ordering_fields = ['name', 'city']
