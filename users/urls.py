from django.urls import path, include
from .views import SignUpView, DeleteUser, Payments, ComplainView, ComplaintsListView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('delete/', DeleteUser.as_view()),
    path('payments/', Payments.as_view()),
    path('', include('dj_rest_auth.urls')),
    path('complain/', ComplainView.as_view()),
    path('complaints/', ComplaintsListView.as_view()),

]
