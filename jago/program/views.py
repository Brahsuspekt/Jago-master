from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def check_result_page(request):
    return render(request, 'main/check_results.html')

def register_courses_page(request):
    return render(request, 'main/register_courses.html')

def registration_history(request):
    return render(request, 'main/registration_history.html')

def fees(request):
    return render(request, 'main/pay_fees.html')

def appointments(request):
    return render(request, 'main/appointments.html')

def file_sharing(request):
    return render(request, 'main/create_docs.html')

