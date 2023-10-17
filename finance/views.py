from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Debts, Expenses
from .serializers import DebtsSerializer, ExpensesSerializer
from users.permissions import HasUserPermission
from courses import models, serializers


class DebtsView(ListCreateAPIView):
    queryset = Debts.objects.all()
    serializer_class = DebtsSerializer
    permission_classes = [HasUserPermission]

    def get(self, request, *args, **kwargs):
        # Get the list of debts
        debts = self.get_queryset()
        overall = 0
        for debt in debts:
            debt_amount = debt.amount
            overall = debt_amount + overall
        serializer = self.get_serializer(debts, many=True)
        response_data = {
            'debts': serializer.data,
            'overall_debts_amount': overall
        }

        return Response(response_data, status=status.HTTP_200_OK)


class ExpensesView(ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [HasUserPermission]

    def get(self, request):
        expenses = self.get_queryset()
        serializer = self.get_serializer(expenses, many=True)
        overall = 0
        for expense in expenses:
            overall = expense.amount + overall
        response_data = {
            'data': serializer.data,
            'overall_expenses_amount': overall
        }
        return Response(response_data, status=status.HTTP_200_OK)


class DebtsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Debts.objects.all()
    serializer_class = DebtsSerializer
    permission_classes = [HasUserPermission]


class ExpensesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [HasUserPermission]


class ProfitsView(APIView):
    def get(self, request):
        students = models.StudentsModel.objects.all()
        overall = 0
        for student in students:
            overall = overall + student.payments

        data = {
            'payments': overall
        }

        return Response(data, status=status.HTTP_200_OK)
