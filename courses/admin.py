from django.contrib import admin
from .models import CoursesModel, GroupsModel, StudentsModel, PaymentsModel

admin.site.register(GroupsModel)
admin.site.register(CoursesModel)
admin.site.register(StudentsModel)
admin.site.register(PaymentsModel)