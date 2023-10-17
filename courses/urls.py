from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoursesView.as_view()),
    path('<int:pk>/', views.CourseView.as_view()),
    path('groups/', views.GroupsView.as_view()),
    path('groups/<int:pk>/', views.GroupView.as_view()),
    path('students/', views.StudentsView.as_view()),
    path('students/<int:pk>/', views.StudentView.as_view()),
    path('payments/', views.PaymentsView.as_view()),
]
