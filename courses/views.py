from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CoursesModel, StudentsModel, GroupsModel, PaymentsModel
from .serializers import CoursesSerializer, GroupsSerializer, PaymentsSerializer, StudentsSerializer


class CoursesView(ListCreateAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer


class CourseView(RetrieveUpdateDestroyAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer


class GroupsView(ListCreateAPIView):
    queryset = GroupsModel.objects.all()
    serializer_class = GroupsSerializer


class GroupView(RetrieveUpdateDestroyAPIView):
    queryset = GroupsModel.objects.all()
    serializer_class = GroupsSerializer


class StudentsView(ListCreateAPIView):
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer


class StudentView(RetrieveUpdateDestroyAPIView):
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer


class PaymentsView(ListCreateAPIView):
    queryset = PaymentsModel.objects.all()
    serializer_class = PaymentsSerializer
