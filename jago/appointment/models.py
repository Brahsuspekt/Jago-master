from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model()


class DayTime(models.Model):
    DAY_LIST = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday")
    ]
    day = models.CharField(choices=DAY_LIST, max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()


class AvailableTime(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    day_and_time = models.ForeignKey(DayTime, on_delete=models.CASCADE) 
    is_active = models.BooleanField(default=True)
     

class Booking(models.Model):
    booker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_booker", null=True, blank=True)
    reserver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_reserver", null=True, blank=True)
    day_time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
