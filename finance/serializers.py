from rest_framework.serializers import ModelSerializer
from .models import Debts, Expenses


class DebtsSerializer(ModelSerializer):
    class Meta:
        model = Debts
        fields = '__all__'


class ExpensesSerializer(ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'
