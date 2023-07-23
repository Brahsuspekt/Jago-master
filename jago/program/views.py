from django.shortcuts import render
from program.models import Course, SharedFile
from django.contrib.auth import get_user_model
from django.contrib import messages 
from program.forms import RegistrationHistoryForm
from appointment.forms import AppointmentForm
from fees.models import Payment, Fees 
from appointment.models import AvailableTime, Booking


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
    payments = Payment.objects.all()
    for payment in payments:
        print(payments.method)
        print('-=-=-=-=-=-=-=-=-=-==')
    
    context = {'payments':payments}
    return render(request, 'main/pay_fees.html', context)


def appointments(request):
    books = Booking.objects.none()
    if request.method == 'POST':
        name = request.POST.get('name')
        lecturer = AvailableTime.objects.get(staff__username=name)
        book = Booking.objects.create(booker=request.user, reserver=lecturer.staff, day_time=lecturer)
        books = Booking.objects.filter(booker=request.user)
    books = Booking.objects.all()
    lecturers = AvailableTime.objects.filter(staff__is_lecturer=True)
    
    context = {'lecturers':lecturers, 'books':books}
    return render(request, 'main/appointments.html', context)

def file_sharing(request):
    user_courses = Course.objects.filter(program__department__user__username=request.user.username)
    for course in user_courses:
        slides = SharedFile.objects.filter(course__name=course.name)
        return render(request, 'main/create_docs.html', {'slides':slides})
    return render(request, 'main/create_docs.html')

