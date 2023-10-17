from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Debts, Expenses
from .serializers import DebtsSerializer, ExpensesSerializer
from users.permissions import HasUserPermission


class DebtsView(ListCreateAPIView):
    queryset = Debts.objects.all()
    serializer_class = DebtsSerializer
    permission_classes = [HasUserPermission]


class ExpensesView(ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [HasUserPermission]


class DebtsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Debts.objects.all()
    serializer_class = DebtsSerializer
    permission_classes = [HasUserPermission]


class ExpensesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [HasUserPermission]