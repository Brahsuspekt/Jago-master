from django.db import models
from program.models import Program
from django.contrib.auth import get_user_model 

User = get_user_model()

# Create your models here.
class Payment(models.Model):
    METHOD_CHOICES = [
        ('MOMO', 'MOMO'),
        ('CARD', 'CARD')
    ]
    CARD_LIST = [
        ('Visa Card', 'Visa Card'),
        ('Master Card', 'Master Card')
    ]
    MOMO_LIST = [
        ('MTN', 'MTN'),
        ('VODAFONE', 'VODAFONE'),
        ('AIRTELTIGO', 'AIRTELTIGO')
    ]
    method = models.CharField(choices=METHOD_CHOICES, max_length=100, null=True, blank=True)
    card_type = models.CharField(choices=CARD_LIST, max_length=100, blank=True, null=True)
    momo_type = models.CharField(choices=MOMO_LIST, max_length=100, blank=True, null=True)
    price = models.FloatField(default=0.0)
    paid = models.BooleanField(default=False)


class Fees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(default=0.0)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)
