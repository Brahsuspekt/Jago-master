from django.shortcuts import render
from program.models import Course
from django.contrib.auth import get_user_model
from django.contrib import messages 
from program.forms import RegistrationHistoryForm

User = get_user_model()


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def check_result_page(request):
    user = request.user 
    courses = Course.objects.filter(program__department__user=user)
    context = {'courses':courses}
    return render(request, 'main/check_results.html', context)


def register_courses_page(request):
    user = request.user 
    courses = Course.objects.none()
    if request.method == 'POST':
        user = User.objects.get(username=user.username)
        user.is_course_registered=True
        user.save()
        courses = Course.objects.filter(program__department__user=user)
        messages.info(request, 'Congratulation Course Has Been Registered!') 
        for course in courses:
            course.status='registered'
            course.save()
    else:
        courses = Course.objects.filter(program__department__user=user)

    context = {'courses': courses}
    return render(request, 'main/register_courses.html', context)


def registration_history(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        courses = Course.objects.filter(year=year, semester=semester)
        context = {'courses':courses}
        return render(request, 'main/registration_history.html', context)
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'main/registration_history.html', context)


def fees(request):
    return render(request, 'main/pay_fees.html')

def appointments(request):
    return render(request, 'main/appointments.html')

def file_sharing(request):
    return render(request, 'main/create_docs.html')

