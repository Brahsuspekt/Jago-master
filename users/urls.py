from django.urls import path 
from users import views


 
urlpatterns = [
    path('account/register/', views.register, name='register'),
    path('account/login/', views.login_view, name='login'),
    path('verify/email/', views.get_user_email, name='send-code'),
    path('verify/code/', views.verify_email, name='verify-code'),
    path('logout/', views.logout_view, name='logout')
]