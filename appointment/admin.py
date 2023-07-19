from django.contrib import admin
from .models import DayTime, AvailableTime, Booking
# Register your models here.
admin.site.site_header = "JAGO CPANEL"
admin.site.site_title = "JAGO CPANEL"

admin.site.register(Booking)
admin.site.register(DayTime)
admin.site.register(AvailableTime)
