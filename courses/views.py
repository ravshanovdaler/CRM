from datetime import datetime, timedelta
from users.permissions import HasUserPermission
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import CoursesModel, StudentsModel, GroupsModel, PaymentsModel
from .serializers import CoursesSerializer, GroupsSerializer, PaymentsSerializer, StudentsSerializer
from rest_framework.response import Response
from rest_framework import status


class CoursesView(ListCreateAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [HasUserPermission]


class CourseView(RetrieveUpdateDestroyAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [HasUserPermission]


class GroupsView(ListCreateAPIView):
    queryset = GroupsModel.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [HasUserPermission]


class GroupView(RetrieveUpdateDestroyAPIView):
    queryset = GroupsModel.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [HasUserPermission]


class StudentsView(ListCreateAPIView):
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [HasUserPermission]


class StudentView(RetrieveUpdateDestroyAPIView):
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [HasUserPermission]


class PaymentsView(ListCreateAPIView):
    queryset = PaymentsModel.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [HasUserPermission]


class DebtorsView(APIView):
    permission_classes = [HasUserPermission]

    def get(self, request):
        debtors = []
        students = StudentsModel.objects.all()
        one_month_ago = datetime.now() - timedelta(days=30)

        for student in students:
            payments = student.payments.filter(date__gte=one_month_ago)

            for payment in payments:
                if payment.date == one_month_ago:
                    paid_in = payment.date
                    debtors.append({'student': student.id, 'amount': payment.amount, 'date': paid_in})

        return Response(debtors, status=status.HTTP_200_OK)
