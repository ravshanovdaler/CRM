from rest_framework.generics import CreateAPIView, DestroyAPIView, ListCreateAPIView
from .permissions import HasUserPermission
from .models import UserModel, SalaryPaymentsModel
from .serializers import UserSerializer, SalaryPayment
from rest_framework.response import Response
from rest_framework import status


class SignUpView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [HasUserPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'You have signed up successfully'}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUser(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [HasUserPermission]
    lookup_field = 'username'


class Payments(ListCreateAPIView):
    queryset = SalaryPaymentsModel.objects.all()
    serializer_class = SalaryPayment
    permission_classes = [HasUserPermission]
