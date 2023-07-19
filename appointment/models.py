from django.db import models
from users.models import CustomUser


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
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    day_and_time = models.ForeignKey(DayTime, on_delete=models.CASCADE) 
    is_active = models.BooleanField(default=True)
     

class Booking(models.Model):
    booker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="booking_booker")
    reserver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="booking_reserver")
    day_time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
