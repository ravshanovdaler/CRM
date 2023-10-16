from django.contrib import admin
from .models import UserModel,SalaryPaymentsModel


admin.site.register(UserModel)
admin.site.register(SalaryPaymentsModel)