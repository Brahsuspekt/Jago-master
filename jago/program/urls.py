from django.urls import path 
from .views import *

app_name="program"

urlpatterns = [
    path("", index, name="index_page"),
    path('check-result', check_result_page, name="check_results_page"),
    path('register-courses', register_courses_page, name="register_courses_page"),
    path('registration-history', registration_history, name="registration_history_page",), 
    path('fees', fees, name="fees_history"),
    path('appointments', appointments, name= "appointments_history"),
    path('file-sharing', file_sharing, name= "file_sharing"),
]