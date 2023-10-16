from rest_framework import serializers
from .models import UserModel, SalaryPaymentsModel
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class SalaryPayment(serializers.ModelSerializer):
    amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = SalaryPaymentsModel
        fields = ('employee', 'amount', 'date')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(min_length=8, style={'input_type': 'password'}, write_only=True)
    payment = SalaryPayment(read_only=True, many=True)

    class Meta:
        model = UserModel
        fields = (
            'username', 'first_name', 'last_name', 'email', 'age', 'phone_number', 'job_type', 'date_employeed',
            'salary',
            'card_number', 'is_paid', 'password', 'password2', 'payment')

    def validate(self, attrs):
        user_exists = UserModel.objects.filter(username=attrs['username']).exists()
        if user_exists:
            raise ValidationError('User already exists')
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise ValidationError('Passwords do not match')

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise ValidationError('Passwords do not match')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
