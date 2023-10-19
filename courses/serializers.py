from rest_framework import serializers
from .models import CoursesModel, GroupsModel, StudentsModel, PaymentsModel


class PaymentsSerializer(serializers.ModelSerializer):
    amount = serializers.CharField(read_only=True)

    class Meta:
        model = PaymentsModel
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True, read_only=True)

    class Meta:
        model = StudentsModel
        fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True, read_only=True)

    class Meta:
        model = GroupsModel
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    groups = GroupsSerializer(many=True, read_only=True)

    class Meta:
        model = CoursesModel
        fields = '__all__'
