from django.urls import path
from . import views


urlpatterns = [
    path('debts/', views.DebtsView.as_view()),
    path('expenses/', views.ExpensesView.as_view()),
    path('expenses/<int:pk>/', views.ExpensesDetailView.as_view()),
    path('debts/<int:pk>/', views.DebtsDetailView.as_view()),
    path('profits/', views.ProfitsView.as_view()),
    path('overall/', views.StatisticsView.as_view())
]