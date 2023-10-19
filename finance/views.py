from datetime import datetime, timedelta

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Debts, Expenses
from .serializers import DebtsSerializer, ExpensesSerializer
from users.permissions import HasUserPermission
from courses.models import PaymentsModel
from courses.serializers import PaymentsSerializer
from users.models import SalaryPaymentsModel
from users.serializers import SalaryPayment


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
    overall = 0

    def get(self, request):
        one_month_ago = datetime.now() - timedelta(days=30)
        payments = PaymentsModel.objects.all()
        payments_data = PaymentsSerializer(payments, many=True)
        for payment in payments:
            if payment.date is not one_month_ago:
                self.overall += payment.amount

        data = {
            'payments': payments_data.data,
            'overall': self.overall

        }

        return Response(data, status=status.HTTP_200_OK)


class StatisticsView(APIView):
    def get(self, request):

        overall_profit_or_loose = 0

        expenses = Expenses.objects.all()
        one_month_ago = datetime.now() - timedelta(days=30)
        overall_expenses = 0
        for expense in expenses:
            if expense.data is not one_month_ago:
                overall_expenses = overall_expenses + expense.amount
        salaries = SalaryPaymentsModel.objects.all()
        overall_salaries = 0
        for salary in salaries:
            if salary.date is not one_month_ago:
                overall_salaries = overall_salaries + salary.amount

        overall_profits = 0

        payments = PaymentsModel.objects.all()
        for payment in payments:
            if payment.date is not one_month_ago:
                overall_profits += payment.amount

        overall_profit_or_loose = overall_profits - overall_salaries - overall_expenses

        if overall_profit_or_loose > 0:
            data = {
                'salary_payments': overall_salaries,
                'expenses': overall_expenses,
                'profits': overall_profits,
                'overall profits': overall_profit_or_loose,
                'status': 'you are making a profit'
            }
            return Response(data, status=status.HTTP_200_OK)

        elif overall_profit_or_loose < 0:
            data = {
                'salary_payments': overall_salaries,
                'expenses': overall_expenses,
                'profits': overall_profits,
                'loses': overall_profit_or_loose,
                'status': 'you are making looses'
            }
            return Response(data, status=status.HTTP_200_OK)

        else:
            data = {
                'salary_payments': overall_salaries,
                'expenses': overall_expenses,
                'profits': overall_profits,
                'status': 'no profit and loss'
            }
            return Response(data, status=status.HTTP_200_OK)
